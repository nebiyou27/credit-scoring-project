import os
import pickle
from flask import Flask, request, jsonify
import numpy as np
from sklearn.preprocessing import StandardScaler

# Initialize Flask app
app = Flask(__name__)

# Path to the Logistic Regression .pkl file
model_path = os.path.join(os.getcwd(), 'tests', 'logistic_regression_model.pkl')  # Dynamic path construction

# Initialize the scaler (make sure it matches the scaler used in training)
scaler = StandardScaler()

# Load the trained Logistic Regression model and scaler
def load_model_and_scaler():
    try:
        # Load Logistic Regression model
        with open(model_path, 'rb') as f:
            log_reg_model = pickle.load(f)

        # If scaler was saved separately, load it as well
        # For now, assuming a new scaler is created during API requests.
        # If you saved the scaler during training, add code to load it similarly.
        return log_reg_model, scaler
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Model file not found at {model_path}")
    except Exception as e:
        raise Exception(f"Error loading the model or scaler: {e}")

# Load model and scaler at the start
try:
    log_reg_model, scaler = load_model_and_scaler()
except Exception as e:
    print(f"Error: {e}")
    log_reg_model, scaler = None, None

@app.route('/')
def home():
    return "Logistic Regression Model API is Running"

@app.route('/predict', methods=['POST'])
def predict():
    if log_reg_model is None or scaler is None:
        return jsonify({'error': 'Model or scaler is not loaded properly'}), 500

    try:
        # Get the input data from the POST request
        data = request.get_json()  # Assuming input data is in JSON format
        
        # Validate input data
        if 'features' not in data:
            return jsonify({'error': 'No "features" key found in the input data'}), 400

        features = np.array(data['features'])

        if features.ndim != 1:
            return jsonify({'error': 'Features must be a one-dimensional array'}), 400

        # Reshape the features for prediction
        features = features.reshape(1, -1)

        # Check if the feature length matches the model's expected input shape
        if features.shape[1] != log_reg_model.n_features_in_:
            return jsonify({'error': f"Expected {log_reg_model.n_features_in_} features, got {features.shape[1]}"}), 400

        # Scale the features
        features_scaled = scaler.transform(features)

        # Make prediction using the Logistic Regression model
        prediction = log_reg_model.predict(features_scaled)

        # Return the prediction as JSON
        return jsonify({'prediction': int(prediction[0])})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
