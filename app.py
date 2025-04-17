import os
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
from flask import Flask, request, render_template, url_for
import flask
from fastai.vision.all import *
app=Flask(__name__)
UPLOAD_FOLDER = r'C:\Users\Hanh\Downloads\F21\Rizk DS\snakes update\pkl_data'

path = Path(UPLOAD_FOLDER)
full_path = os.path.join(path, 'snake.pkl')
print(full_path)
model = load_learner(full_path)
def predict_img(image_file, model):
    image_path = os.path.join(path, UPLOAD_FOLDER, image_file.filename)
    img = PILImage.create(image_path)
    pred, pred_id, probs = model.predict(img)
    print(pred_id)
    print(probs[pred_id])
    return pred, probs[pred_id]

@app.route('/', methods=['GET', 'POST'])
def upload_predict():
    # if only post
    if request.method == 'POST':
        # gets image in the image file
        image_file = request.files['image']
        if image_file:
            # this concats the directory and image file as a path to be saved
            image_location = os.path.join(UPLOAD_FOLDER, image_file.filename)
            # now we save the image
            image_file.save(image_location)
            prediction, probability = predict_img(image_file, model)
            confidence=round((probability.numpy())*100,2)
            return render_template('index.html', prediction=prediction, uploaded_img=image_file.filename,probability=confidence)
    return render_template('index.html', uploaded_img=None)

if __name__ == '__main__':
    app.run(debug=True)
'''
model = load_learner(full_path)
def predict_img(image_file, model):
    image_path = os.path.join(path, UPLOAD_FOLDER, image_file.filename)
    img = PILImage.create(image_path)
    pred, pred_id, probs = model.predict(img)
    return pred, probs[pred_id]

@app.route('/', methods=['GET', 'POST'])
def upload_predict():
    # if only post
    if request.method == 'POST':
        # gets image in the image file
        image_file = request.files['image']
        if image_file:
            # this concats the directory and image file as a path to be saved
            image_location = os.path.join(UPLOAD_FOLDER, image_file.filename)
            # now we save the image
            image_file.save(image_location)
            prediction, probability = predict_img(image_file, model)
            return render_template('index.html', prediction=prediction, uploaded_img=image_file.filename)
    return render_template('index.html', uploaded_img=None)

if __name__ == '__main__':
    app.run(debug=True)
'''