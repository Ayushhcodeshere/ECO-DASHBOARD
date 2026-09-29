import streamlit as st
import plotly.graph_objects as go
from utils.data_gen import get_hourly_consumption_data, get_monthly_trend_data
from utils.charts import plot_energy_trend

def render():
    """
    Renders the Predictive Analytics page, showing hourly, daily,
    and monthly forecasts of energy consumption.
    """
    st.title("🔮 Predictive Analytics")
    st.markdown("Forecasts based on historical data and AI models.")
    
    tabs = st.tabs(["Hourly Forecast", "Daily Forecast", "Monthly Forecast"])
    
    with tabs[0]:
        st.subheader("24-Hour Forecast")
        hourly_data = get_hourly_consumption_data(days=2) # 48 hours for context
        fig = plot_energy_trend(hourly_data)
        st.plotly_chart(fig, use_container_width=True)
        st.info("Peak expected tomorrow between 14:00 and 16:00. Consider pre-cooling to save costs.")
        
    with tabs[1]:
        st.subheader("7-Day Forecast")
        # Reuse same function for simplicity, pretend it's daily data
        daily_data = get_hourly_consumption_data(days=7) 
        fig = plot_energy_trend(daily_data)
        fig.update_layout(title="Daily Consumption Trend (Actual vs Predicted)")
        st.plotly_chart(fig, use_container_width=True)
        
    with tabs[2]:
        st.subheader("Monthly Historical Trend")
        monthly_data = get_monthly_trend_data()
        
        fig = go.Figure()
        fig.add_trace(go.Bar(x=monthly_data['Month'], y=monthly_data['Actual'], 
                             name='Actual (kWh)', marker_color='#4cc9f0'))
        fig.add_trace(go.Scatter(x=monthly_data['Month'], y=monthly_data['Predicted'], mode='lines+markers', 
                                 name='Predicted (kWh)', line=dict(color='#f72585', width=3)))
                                 
        fig.update_layout(
            template="plotly_dark",
            xaxis_title="Month",
            yaxis_title="Energy Consumption (kWh)",
            hovermode="x unified"
        )
        st.plotly_chart(fig, use_container_width=True)
