"""
Snake Bite Prediction System - Simplified Version
Works without FastAI model for demo purposes
"""

import os
import datetime
import random
from flask import Flask, request, render_template, session, send_from_directory
from PIL import Image

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'snake_prediction_deep_learning_2026'

# Configuration
UPLOAD_FOLDER = os.path.join('static', 'uploads')

# Create upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Snake species database
SNAKE_DATABASE = {
    "Northern Cottonmouth": {
        "scientific_name": "Agkistrodon piscivorus",
        "venomous": True,
        "danger_level": "High",
        "description": "Also known as Water Moccasin. A highly venomous pit viper found in southeastern United States. Recognizable by its distinctive white mouth interior which it displays when threatened.",
        "habitat": "Swamps, marshes, and slow-moving streams",
        "first_aid": "Seek immediate medical attention. Keep victim calm and immobilize the affected limb. Do NOT apply ice or tourniquet.",
        "color": "#ef4444"
    },
    "Texas Coral Snake": {
        "scientific_name": "Micrurus tener",
        "venomous": True,
        "danger_level": "Extreme",
        "description": "Highly venomous elapid snake with distinctive red, yellow, and black bands. Remember: 'Red on yellow, kill a fellow.' Possesses potent neurotoxic venom.",
        "habitat": "Wooded areas, rocky hillsides, and leaf litter",
        "first_aid": "IMMEDIATE medical emergency! Call 911. Keep victim still and calm. Neurotoxic venom affects nervous system.",
        "color": "#dc2626"
    },
    "Plain Bellied Water Snake": {
        "scientific_name": "Nerodia erythrogaster",
        "venomous": False,
        "danger_level": "Low",
        "description": "Non-venomous water snake often mistaken for Cottonmouth. Harmless to humans. Excellent swimmers and fish hunters. May bite if provoked but not dangerous.",
        "habitat": "Rivers, lakes, ponds, and wetlands",
        "first_aid": "Clean wound with soap and water. Apply antiseptic. Monitor for infection. Not dangerous.",
        "color": "#22c55e"
    },
    "Louisiana Milk Snake": {
        "scientific_name": "Lampropeltis triangulum amaura",
        "venomous": False,
        "danger_level": "Low",
        "description": "Non-venomous king snake that mimics the Coral Snake's appearance. Remember: 'Red on black, friend of Jack.' Completely harmless and beneficial for pest control.",
        "habitat": "Forests, grasslands, and rocky areas",
        "first_aid": "Clean wound if bitten. Apply antiseptic. Completely harmless to humans.",
        "color": "#10b981"
    }
}

def predict_snake(image_path):
    """Demo prediction function"""
    species = list(SNAKE_DATABASE.keys())
    pred = random.choice(species)
    confidence = random.uniform(75.0, 95.0)
    return pred, confidence

@app.route('/', methods=['GET', 'POST'])
def index():
    """Main page"""
    if 'history' not in session:
        session['history'] = []
    
    if request.method == 'POST':
        if 'snake_image' not in request.files:
            return render_template('index.html', error="No image uploaded", history=session.get('history', []))
        
        image_file = request.files['snake_image']
        
        if image_file.filename == '':
            return render_template('index.html', error="No image selected", history=session.get('history', []))
        
        if image_file:
            # Save uploaded image
            filename = f"snake_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            image_file.save(filepath)
            
            # Predict
            species, confidence = predict_snake(filepath)
            snake_info = SNAKE_DATABASE[species]
            
            # Create result
            result = {
                'species': species,
                'confidence': round(confidence, 2),
                'scientific_name': snake_info['scientific_name'],
                'venomous': snake_info['venomous'],
                'danger_level': snake_info['danger_level'],
                'description': snake_info['description'],
                'habitat': snake_info['habitat'],
                'first_aid': snake_info['first_aid'],
                'color': snake_info['color'],
                'image_url': f'uploads/{filename}',
                'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            # Add to history
            history = session.get('history', [])
            history.insert(0, {
                'species': species,
                'confidence': round(confidence, 2),
                'venomous': snake_info['venomous'],
                'timestamp': datetime.datetime.now().strftime('%H:%M'),
                'image_url': f'uploads/{filename}'
            })
            session['history'] = history[:10]
            
            return render_template('index.html', result=result, history=session.get('history', []))
    
    return render_template('index.html', history=session.get('history', []))

@app.route('/about')
def about():
    return render_template('about.html', history=session.get('history', []))

@app.route('/species')
def species():
    return render_template('species.html', snakes=SNAKE_DATABASE, history=session.get('history', []))

@app.route('/safety')
def safety():
    return render_template('safety.html', history=session.get('history', []))

@app.route('/statistics')
def statistics():
    """Statistics dashboard"""
    history = session.get('history', [])
    
    # Calculate stats
    total_scans = len(history)
    venomous_count = sum(1 for scan in history if scan.get('venomous', False))
    harmless_count = total_scans - venomous_count
    
    # Species breakdown
    species_count = {}
    for scan in history:
        species = scan.get('species', 'Unknown')
        species_count[species] = species_count.get(species, 0) + 1
    
    stats = {
        'total_scans': total_scans,
        'venomous_count': venomous_count,
        'harmless_count': harmless_count,
        'species_breakdown': species_count,
        'venomous_percentage': round((venomous_count / total_scans * 100) if total_scans > 0 else 0, 1),
        'harmless_percentage': round((harmless_count / total_scans * 100) if total_scans > 0 else 0, 1)
    }
    
    return render_template('statistics.html', stats=stats, history=history)

@app.route('/emergency')
def emergency():
    """Emergency contact page"""
    return render_template('emergency.html', history=session.get('history', []))

@app.route('/quiz')
def quiz():
    """Snake facts quiz"""
    return render_template('quiz.html', history=session.get('history', []))

@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    import os
    
    # Use port 7860 for Hugging Face Spaces, 5001 for local
    port = int(os.environ.get('PORT', 7860))
    
    print("\n" + "="*60)
    print("🐍 Snake Bite Prediction System using Deep Learning")
    print("="*60)
    print("✓ Flask app initialized")
    print(f"✓ Upload folder: {UPLOAD_FOLDER}")
    print("✓ Demo mode active (random predictions)")
    print("="*60)
    print("\n🌐 Starting server...")
    print(f"📍 Server running on port: {port}")
    print("\n⌨️  Press CTRL+C to stop the server\n")
    
    # Bind to 0.0.0.0 for Hugging Face, use port from environment
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)

