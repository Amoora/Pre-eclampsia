from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open("model.pkl","rb"))


@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = ''
    if request.method == 'POST':
        # Extract features from the form
        feature1 = request.form.get('Age', type=float)
        feature2 = request.form.get('Urinalysis', type=float)
        feature3 = request.form.get('Pcv', type=float)
        feature4 = request.form.get('Gestational_Age', type=float)
        feature5 = request.form.get('Blood_GroupBG', type=float)
        feature6 = request.form.get('HCV', type=float)
        feature7 = request.form.get('RVS', type=float)
        feature8 = request.form.get('PRbm', type=float)
        feature9 = request.form.get('History_of_emclapsia_in_family', type=float)
        feature10 = request.form.get('HBSAG', type=float)
        feature11 = request.form.get('systolic_bp', type=float)
        feature12 = request.form.get('diastolic_bp', type=float)



        # Make prediction
        prediction = model.predict([[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10, feature11, feature12]])[0]
        if prediction == 0:
            prediction = f'The prediction is not eclamsia {prediction}'
        else: prediction = f'The prediction is Eclampsia {prediction}'

    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
