import os
import sys

# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# TensorFlow and tf.keras

# Some utilites
import numpy as np
from util import base64_to_pil


# Declare a flask app
app = Flask(__name__)
# app.debug = True



def model_predict(img):
    img = img.resize((224, 224))

    # Preprocessing the image
   
    preds="pandas"
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('image.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the image from post request
        img = base64_to_pil(request.json)

        # Save the image to ./uploads
        # img.save("./uploads/image.png")

        # Make prediction
        preds = model_predict(img)

        # Process your result for human
        pred_proba = 0.3    # Max probability
        pred_class = preds  # ImageNet Decode

        # result = str(pred_class[0][0][1])               # Convert to string
        result =pred_class
        
        # = result.replace('_', ' ').capitalize()
        
        # Serialize the result, you can add additional fields
        return jsonify(result=result, probability=pred_proba)

    return None


if __name__ == '__main__':
    # app.run(port=5002, threaded=False)

    # Serve the app with gevent
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
