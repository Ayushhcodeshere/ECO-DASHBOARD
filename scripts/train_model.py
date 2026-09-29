import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import os

print("Starting model training process...")

# Ensure directories exist
os.makedirs('models', exist_ok=True)
os.makedirs('data', exist_ok=True)

# Load data
data_path = "data/cleaned_data.csv"
if not os.path.exists(data_path):
    # Fallback to original location
    data_path = "individual+household+electric+power+consumption (1)/individual+household+electric+power+consumption (1)/data/cleaned_data.csv"
    
print(f"Loading data from {data_path}...")
df = pd.read_csv(data_path)

print("Preparing features...")
df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], dayfirst=True)
df['Hour'] = df['Datetime'].dt.hour
df['Day'] = df['Datetime'].dt.day
df['Month'] = df['Datetime'].dt.month
df['DayOfWeek'] = df['Datetime'].dt.dayofweek
df['Previous_Consumption'] = df['Global_active_power'].shift(1)

df.dropna(inplace=True)

# Save feature data for later use by data_gen
df.to_csv("data/feature_data.csv", index=False)

y = df['Global_active_power']
X = df[[
    'Hour', 'Day', 'Month', 'DayOfWeek', 'Voltage', 
    'Global_intensity', 'Sub_metering_1', 'Sub_metering_2', 
    'Sub_metering_3', 'Previous_Consumption'
]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Use a small subset to train fast (as done in the notebook)
print("Training model...")
X_small = X_train.iloc[:50000]
y_small = y_train.iloc[:50000]

rf_model = RandomForestRegressor(n_estimators=30, random_state=42, n_jobs=-1)
rf_model.fit(X_small, y_small)

print("Saving model to models/energy_model.pkl...")
joblib.dump(rf_model, "models/energy_model.pkl")

print("Training complete!")
