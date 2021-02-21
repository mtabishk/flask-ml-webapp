import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import joblib
import json

app = Flask(__name__)

model = joblib.load('50Startupsmodel.pk1')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/output',methods=['POST'])
def output():
    rnd = float(request.form['rnd'])
    admin = float(request.form['admin'])
    market = float(request.form['market'])
    state = str(request.form['state'])
    
    res = { "rnd": rnd, "admin": admin, "market": market, "state": state }
    return json.dumps(res)


@app.route('/predict',methods=['POST'])
def predict():
    rnd = float(request.form['rnd'])
    admin = float(request.form['admin'])
    market = float(request.form['market'])
    state = str(request.form['state'])
    
    state_florida = 0
    state_newyork = 0
    if state == "Florida" or state == "florida":
        state_florida = 1
    elif state == "New York" or "new york":
        state_newyork = 1
    
    res = model.predict([[rnd, admin, market, state_florida, state_newyork]])
    res = float(res)

    return render_template('index.html', prediction_text='Profit = {}'.format(res))


if __name__ == "__main__":
    app.run(debug=True)
