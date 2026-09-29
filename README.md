# ⚡ AI Energy Optimizer - ECO Dashboard

An interactive Streamlit web dashboard powered by Machine Learning to monitor household energy consumption, forecast future power usage, provide energy-saving recommendations, and simulate efficiency scenarios.

---

## 🚀 Features

- **📊 Overview Dashboard**: Real-time energy consumption metrics, sub-metering breakdown (kitchen, laundry, HVAC), and key usage indicators.
- **🔮 Predictive Forecasting**: Machine Learning model predictions for future power consumption trends.
- **📈 Deep Analysis**: Exploratory historical consumption trends, peak-load analysis, and anomaly detection.
- **💡 Smart Recommendations**: Personalized, actionable tips to reduce electricity bills and lower carbon footprint.
- **🎛️ Scenario Simulator**: What-if simulation tool to calculate savings by changing household habits or switching appliances.
- **🎯 Goals & Progress**: Monthly energy reduction targets and tracking against sustainability goals.
- **⚙️ Settings & Reports**: Customizable parameters, reporting configurations, and export options.

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Visualizations**: [Plotly](https://plotly.com/python/)
- **Machine Learning**: [scikit-learn](https://scikit-learn.org/)
- **Data Processing**: [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)

---

## 📂 Project Structure

```text
ECO DASHBOARD/
│
├── app.py                # Main Streamlit application entry point
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── .gitignore            # Git ignore file
│
├── views/                # Streamlit UI page views
│   ├── dashboard.py      # Main dashboard view
│   ├── prediction.py     # Power consumption forecasting view
│   ├── analysis.py       # Data analysis & charts
│   ├── recommendations.py# Energy efficiency suggestions
│   ├── simulator.py      # What-if scenario simulator
│   ├── goals.py          # Carbon & energy goal tracking
│   └── settings.py       # User preferences and export settings
│
├── utils/                # Utility modules
│   ├── charts.py         # Plotly visualization builders
│   ├── data_gen.py       # Data generators and transformations
│   ├── models.py         # Model loading and inference helper
│   └── recommendations_engine.py # Rule-based & ML recommendation logic
│
├── scripts/              # Training & data prep scripts
│   └── train_model.py    # Model training pipeline
│
└── models/               # Serialized ML model artifacts (energy_model.pkl)
```

---

## 💻 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Ayushhcodeshere/ECO-DASHBOARD.git
cd ECO-DASHBOARD
```

### 2. Create and activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`.

---

## 📄 License

This project is licensed under the MIT License.
