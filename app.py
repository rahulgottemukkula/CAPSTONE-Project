from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model from the .pkl file
model = pickle.load(open('Heart Disease Prediction Using ML Algos/best_model.pkl', 'rb'))

# Define a route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for the prediction page
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the user's input data from the form
        data = request.form.to_dict()

        # Convert the form data values from strings to appropriate types
        data = {key: float(value) for key, value in data.items()}

        # Convert the input data into a pandas DataFrame
        input_df = pd.DataFrame([data])

        # If using predict_proba to get the probability of heart disease
        risk_prob = model.predict_proba(input_df)[0][1]  # Assuming index 1 is for 'heart disease' class
        
        # Convert risk probability to percentage
        risk_percentage = round(risk_prob * 100, 2)
        
        # Define risk label based on risk percentage
        risk_label = "High Risk" if risk_percentage > 50 else "Low Risk"
        
        # Render the result page with the risk percentage and label
        return render_template('result.html', risk_percentage=risk_percentage, risk_label=risk_label)
    else:
        return render_template('predict.html')


if __name__ == '__main__':
    app.run(debug=True)
