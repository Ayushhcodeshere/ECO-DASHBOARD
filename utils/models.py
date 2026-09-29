import numpy as np
import pandas as pd
import joblib
import os
import streamlit as st

@st.cache_resource
def load_prediction_model():
    """
    Loads the trained ML model (Random Forest) from the models directory.
    Uses st.cache_resource to avoid reloading it on every interaction.
    """
    model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models', 'energy_model.pkl')
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        # Fallback to dummy model if loading fails
        class DummyModel:
            def predict(self, X):
                return np.random.uniform(5, 10, len(X))
        return DummyModel()

def predict_energy_usage(features_df):
    """
    Wrapper function to pass features to the loaded ML model and get predictions.
    Expected features: ['Hour', 'Day', 'Month', 'DayOfWeek', 'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3', 'Previous_Consumption']
    """
    model = load_prediction_model()
    # Ensure features_df matches model expected inputs exactly
    expected_cols = [
        'Hour', 'Day', 'Month', 'DayOfWeek', 'Voltage', 
        'Global_intensity', 'Sub_metering_1', 'Sub_metering_2', 
        'Sub_metering_3', 'Previous_Consumption'
    ]
    
    # Fill missing columns with 0 if any (just as a safety net)
    for col in expected_cols:
        if col not in features_df.columns:
            features_df[col] = 0
            
    predictions = model.predict(features_df[expected_cols])
    return predictions

def detect_anomalies(current_usage, average_usage, threshold=1.5):
    """
    Simple anomaly detection logic. Returns True if current usage is unexpectedly high.
    Can be replaced with an Isolation Forest or similar ML anomaly detection model.
    """
    if current_usage > (average_usage * threshold):
        return True, ((current_usage - average_usage) / average_usage) * 100
    return False, 0
