from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
with open('xgb_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html', data={})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    data = {k: float(v) for k, v in data.items()}
    df = pd.DataFrame(data, index=[0])
    prediction = model.predict(df)
    result = 'Failure' if prediction[0] == 1 else 'No Failure'
    return render_template('index.html', prediction_text=f'Prediction: {result}', data=data)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
