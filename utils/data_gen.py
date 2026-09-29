import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
import streamlit as st
from utils.models import predict_energy_usage

@st.cache_data
def load_historical_data():
    """Loads historical data, cached to avoid reading the large CSV repeatedly."""
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'feature_data.csv')
    try:
        df = pd.read_csv(data_path)
        df['Datetime'] = pd.to_datetime(df['Datetime'])
        return df
    except Exception as e:
        st.error(f"Error loading historical data: {e}")
        return pd.DataFrame()

def get_hourly_consumption_data(days=1):
    """Generates hourly consumption data using actuals and ML predictions."""
    df = load_historical_data()
    if df.empty:
        return pd.DataFrame()
        
    minutes = days * 24 * 60
    
    # Take the most recent 'minutes' rows to represent our "current" context
    slice_df = df.iloc[-minutes:].copy() if len(df) > minutes else df.copy()
        
    # Predict using the ML model
    slice_df['Predicted'] = predict_energy_usage(slice_df)
    
    # Aggregate from minute-level to hourly
    slice_df.set_index('Datetime', inplace=True)
    hourly = slice_df.resample('h').agg({
        'Global_active_power': 'sum',
        'Predicted': 'sum'
    }).reset_index()
    
    hourly.rename(columns={'Global_active_power': 'Actual', 'Datetime': 'Timestamp'}, inplace=True)
    
    # Shift timestamps so the latest data point is "now" for a realistic dashboard feel
    if not hourly.empty:
        time_diff = datetime.now() - hourly['Timestamp'].max()
        hourly['Timestamp'] = hourly['Timestamp'] + time_diff
    
    return hourly

def get_current_metrics():
    """Calculates current metrics based on recent historical data and predictions."""
    df = load_historical_data()
    if df.empty:
        return {
            "today_consumption": 0, "today_delta": 0, 
            "predicted_tomorrow": 0, "tomorrow_delta": 0, 
            "month_consumption": 0, "month_delta": 0, 
            "estimated_bill": 0, "bill_delta": 0, "efficiency_score": 0
        }
        
    # 1 day = 1440 mins
    today_df = df.iloc[-1440:]
    yesterday_df = df.iloc[-2880:-1440]
    
    today_sum = today_df['Global_active_power'].sum()
    yesterday_sum = yesterday_df['Global_active_power'].sum()
    
    today_delta = ((today_sum - yesterday_sum) / yesterday_sum * 100) if yesterday_sum else 0
    
    # Predict tomorrow (using today's features as a base proxy)
    predicted_tomorrow = predict_energy_usage(today_df).sum()
    tomorrow_delta = ((predicted_tomorrow - today_sum) / today_sum * 100) if today_sum else 0
    
    # Monthly calculations
    month_sum = df.iloc[-43200:]['Global_active_power'].sum()
    last_month_sum = df.iloc[-86400:-43200]['Global_active_power'].sum()
    month_delta = ((month_sum - last_month_sum) / last_month_sum * 100) if last_month_sum else 0
    
    # Bill estimation (assuming rate of ₹8 per kWh)
    rate = 8
    estimated_bill = month_sum * rate
    bill_delta = (month_sum - last_month_sum) * rate
    
    efficiency_score = max(0, min(100, 100 - (today_delta * 1.5)))
    
    return {
        "today_consumption": round(today_sum, 2),
        "today_delta": round(today_delta, 1),
        "predicted_tomorrow": round(predicted_tomorrow, 2),
        "tomorrow_delta": round(tomorrow_delta, 1),
        "month_consumption": round(month_sum, 2),
        "month_delta": round(month_delta, 1),
        "estimated_bill": int(estimated_bill),
        "bill_delta": int(bill_delta),
        "efficiency_score": int(efficiency_score)
    }

def get_appliance_usage():
    """Mock data for appliance usage (would require sub-metering breakdown in a real scenario)."""
    # We could use Sub_metering_1, 2, 3 here, but the dashboard expects specific appliances
    df = load_historical_data()
    if not df.empty:
        latest = df.iloc[-43200:] # Last month
        sub1 = latest['Sub_metering_1'].sum() # Kitchen
        sub2 = latest['Sub_metering_2'].sum() # Laundry
        sub3 = latest['Sub_metering_3'].sum() # Water heater & AC
        total = latest['Global_active_power'].sum() * 1000 / 60 # Convert to watt-hours approx
        others = max(0, total - (sub1 + sub2 + sub3))
        
        data = {
            "Appliance": ["Kitchen", "Laundry", "AC/Water Heater", "Others"],
            "Consumption (kWh)": [round(sub1/1000, 1), round(sub2/1000, 1), round(sub3/1000, 1), round(others/1000, 1)]
        }
    else:
        data = {
            "Appliance": ["AC", "Refrigerator", "TV", "Lighting", "Others"],
            "Consumption (kWh)": [65.2, 35.5, 15.0, 12.8, 24.1]
        }
    return pd.DataFrame(data)

def get_monthly_trend_data():
    """Aggregates monthly trend data and predictions."""
    df = load_historical_data()
    if df.empty:
        return pd.DataFrame()
        
    # Analyze the last year of data to be fast
    last_year = df.iloc[-500000:].copy() # Roughly 1 year of minute data
    if not last_year.empty:
        last_year['Predicted'] = predict_energy_usage(last_year)
        last_year.set_index('Datetime', inplace=True)
        # Use 'ME' for month end frequency
        monthly = last_year.resample('ME').agg({
            'Global_active_power': 'sum',
            'Predicted': 'sum'
        }).reset_index()
        
        # Keep last 12 months
        monthly = monthly.iloc[-12:]
        monthly['Month'] = monthly['Datetime'].dt.strftime('%b')
        monthly.rename(columns={'Global_active_power': 'Actual'}, inplace=True)
        
        return monthly[['Month', 'Actual', 'Predicted']]
    
    return pd.DataFrame()
