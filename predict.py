# src/predict.py

import joblib
import numpy as np

# Load model & scaler (global load for efficiency)
model = joblib.load("heart_model.pkl")
scaler = joblib.load("scaler.pkl")


def predict_heart_disease(input_data: list):
    """
    input_data: list of feature values
    returns: prediction (0 or 1)
    """

    # Convert to numpy array
    input_array = np.array(input_data).reshape(1, -1)

    # Scale input
    input_scaled = scaler.transform(input_array)

    # Prediction
    prediction = model.predict(input_scaled)

    return int(prediction[0])