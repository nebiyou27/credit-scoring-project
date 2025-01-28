import pickle
from flask import Flask, request, jsonify
import numpy as np
from sklearn.preprocessing import StandardScaler
import os

# Initialize Flask app
app = Flask(__name__)

# Path to the Logistic Regression .pkl file
model_path = r"C:\Users\neba\Documents\credit-scoring-project\tests\logistic_regression_model.pkl"

# Load the trained Logistic Regression model
with open(model_path, 'rb') as f:
    log_reg_model = pickle.load(f)

# Initialize the scaler (make sure it matches the scaler used in training)
scaler = StandardScaler()

@app.route('/')
def home():
    return "Logistic Regression Model API is Running"

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the POST request
    data = request.get_json()  # Assuming input data is in JSON format
    
    # Extract features from the JSON data
    features = np.array(data['features']).reshape(1, -1)
    
    # Scale the features
    features_scaled = scaler.transform(features)  # Use the same scaler that was used in training

    # Make prediction using the Logistic Regression model
    prediction = log_reg_model.predict(features_scaled)
    
    # Return the prediction as JSON
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
