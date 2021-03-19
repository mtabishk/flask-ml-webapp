from keras.models import load_model
from flask import Flask, render_template, request

model = load_model("diabetes_model.h5")
app = Flask("diabetes_model_app")

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
	no_pregnent = float(request.form['no_pregnent'])	
	plasma_glucose_conc = float(request.form['plasma_glucose_conc'])	
	diastolic_bp = float(request.form['diastolic_bp'])	
	triceps_skinfold_thickness = float(request.form['triceps_skinfold_thickness'])	
	serum_insulin = float(request.form['serum_insulin'])	
	bmi = float(request.form['bmi'])	
	diabetes_pedigree_fn = float(request.form['diabetes_pedigree_fn'])	
	age = float(request.form['age'])
	
	output = model.predict( [[no_pregnent, plasma_glucose_conc, diastolic_bp, triceps_skinfold_thickness, serum_insulin, bmi, diabetes_pedigree_fn, age
] ])
	if str(round(output[0][0])) == '0':
		prediction_text = 'Dead'
	else:
		prediction_text	= 'Alive'

	return  render_template("result.html", prediction_text= prediction_text )
 


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000, debug=True)
