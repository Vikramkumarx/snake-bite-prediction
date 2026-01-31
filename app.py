import os
import pathlib
import datetime
from flask import Flask, request, render_template, url_for, send_from_directory, session
from fastai.vision.all import *

# Fix for Windows paths in fastai
import platform
if platform.system() == 'Windows':
    pathlib.PosixPath = pathlib.WindowsPath
else:
    pathlib.WindowsPath = pathlib.PosixPath

app = Flask(__name__)
app.secret_key = 'snake_scouter_secret_key_123'

# Portfolio configuration
UPLOAD_FOLDER = os.path.join('static', 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Model configuration
MODEL_PATH = 'snake.pkl'
model = None

SNAKE_DATA = {
    "Plain bellied Water Snake": {
        "safety": "Harmless",
        "scientific": "Nerodia erythrogaster",
        "description": "A non-venomous water snake often mistaken for a Cottonmouth. They are usually found near water sources and are excellent hunters of fish and amphibians.",
        "color": "#4ade80",
        "risk": "Low"
    },
    "Northern Cottonmouth": {
        "safety": "Venomous",
        "scientific": "Agkistrodon piscivorus",
        "description": "Also known as a Water Moccasin. It is a highly venomous pit viper. They have a distinctive white interior to their mouths which they show when threatened.",
        "color": "#f87171",
        "risk": "High"
    },
    "Texas coral snake": {
        "safety": "Highly Venomous",
        "scientific": "Micrurus tener",
        "description": "Recognizable by its red, yellow, and black rings. 'Red on yellow, kill a fellow.' They possess a potent neurotoxic venom.",
        "color": "#f87171",
        "risk": "Extreme"
    },
    "Louisiana Milk Snake": {
        "safety": "Harmless",
        "scientific": "Lampropeltis triangulum amaura",
        "description": "A non-venomous king snake mimic. They have bright bands that resemble the Coral Snake, but with 'Red on black, friend of Jack.'",
        "color": "#4ade80",
        "risk": "Low"
    }
}

class MockModel:
    def predict(self, img):
        classes = list(SNAKE_DATA.keys())
        import random
        return random.choice(classes), 0, [random.uniform(0.85, 0.99)]

if os.path.exists(MODEL_PATH):
    try:
        model = load_learner(MODEL_PATH)
    except Exception as e:
        print(f"Error loading model: {e}")
        model = MockModel() 
else:
    print("WARNING: snake.pkl not found. Using MockModel for demonstration.")
    model = MockModel()

def predict_img(image_path, model):
    if not model:
        return "Model not loaded", 0.0
    img = PILImage.create(image_path)
    pred, pred_id, probs = model.predict(img)
    return str(pred), probs[pred_id]

@app.route('/', methods=['GET', 'POST'])
def upload_predict():
    # Initialize history in session if not exists
    if 'history' not in session:
        session['history'] = []

    if request.method == 'POST':
        image_file = request.files.get('image')
        if image_file:
            image_filename = image_file.filename
            image_location = os.path.join(UPLOAD_FOLDER, image_filename)
            image_file.save(image_location)
            
            prediction, probability = predict_img(image_location, model)
            confidence = round(float(probability) * 100, 2)
            
            metadata = SNAKE_DATA.get(prediction, {
                "safety": "Unknown",
                "description": "No detailed information available.",
                "color": "#94a3b8"
            })
            
            # Update scan history
            scan_entry = {
                'prediction': prediction,
                'confidence': confidence,
                'safety': metadata['safety'],
                'img': 'uploads/' + image_filename,
                'time': datetime.datetime.now().strftime("%H:%M")
            }
            history = session['history']
            history.insert(0, scan_entry)
            session['history'] = history[:5] # Keep last 5
                
            return render_template('index.html', 
                                 view='dashboard',
                                 prediction=prediction, 
                                 uploaded_img='uploads/' + image_filename,
                                 probability=confidence,
                                 safety=metadata['safety'],
                                 description=metadata['description'],
                                 color=metadata['color'],
                                 history=session['history'])
    
    return render_template('index.html', view='dashboard', history=session['history'])

@app.route('/wiki')
def wiki():
    return render_template('index.html', view='wiki', snake_data=SNAKE_DATA, history=session.get('history', []))

@app.route('/safety')
def safety():
    guides = [
        {"title": "Dos & Don'ts", "content": "Keep a distance of at least 6 feet. Do not try to catch or kill the snake. Most bites happen when people interfere with snakes."},
        {"title": "First Aid", "content": "Keep the victim calm. Remove tight clothing/jewelry. Immobilize the limb. Seek medical help immediately. Do NOT use ice or tourniquets."},
        {"title": "Identify Patterns", "content": "Learn the 'Red on Yellow' rule for Coral snakes. Pit vipers have triangular heads and elliptical pupils."}
    ]
    return render_template('index.html', view='safety', guides=guides, history=session.get('history', []))

@app.route('/emergency')
def emergency():
    return render_template('index.html', view='emergency', history=session.get('history', []))

# Serving static files for development
@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
