import streamlit as st
from utils.data_gen import get_current_metrics, get_hourly_consumption_data, get_appliance_usage
from utils.charts import plot_energy_trend, plot_appliance_usage
from utils.models import detect_anomalies

def render():
    """
    Renders the Overview Dashboard page containing top KPI cards,
    real-time energy consumption trends, and appliance usage charts.
    """
    st.title("📊 Overview Dashboard")
    st.markdown("Monitor your real-time energy consumption and view AI-driven insights.")
    
    # Load mock data
    metrics = get_current_metrics()
    hourly_data = get_hourly_consumption_data(days=1)
    appliance_data = get_appliance_usage()
    
    # Check for anomalies
    current_today = metrics["today_consumption"]
    normal_avg = 5.50 # Hardcoded for demo purposes
    is_anomaly, pct_diff = detect_anomalies(current_today, normal_avg)
    
    if is_anomaly:
        st.error(f"⚠️ **HIGH CONSUMPTION DETECTED**: Today's Usage is {current_today:.2f} kWh vs Normal Avg {normal_avg:.2f} kWh (+{pct_diff:.0f}%)")
    
    # Top KPI Cards
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(label="Today's Consumption", 
                  value=f"{metrics['today_consumption']} kWh", 
                  delta=f"{metrics['today_delta']}% vs yesterday", 
                  delta_color="inverse")
                  
    with col2:
        st.metric(label="Predicted Tomorrow", 
                  value=f"{metrics['predicted_tomorrow']} kWh", 
                  delta=f"{metrics['tomorrow_delta']}% vs today", 
                  delta_color="inverse")
                  
    with col3:
        st.metric(label="This Month So Far", 
                  value=f"{metrics['month_consumption']} kWh", 
                  delta=f"{metrics['month_delta']}% vs last month", 
                  delta_color="inverse")
                  
    with col4:
        st.metric(label="Estimated Bill", 
                  value=f"₹{metrics['estimated_bill']}", 
                  delta=f"₹{metrics['bill_delta']} vs last month", 
                  delta_color="inverse")
                  
    with col5:
        # Simple string for now, could be a gauge chart in Plotly
        st.metric(label="Efficiency Score", 
                  value=f"{metrics['efficiency_score']} / 100", 
                  delta="Good", 
                  delta_color="normal")
                  
    st.markdown("---")
    
    # Main Charts
    st.subheader("Energy Consumption Trends")
    col_chart1, col_chart2 = st.columns([2, 1])
    
    with col_chart1:
        # Line chart for energy trend
        trend_fig = plot_energy_trend(hourly_data)
        st.plotly_chart(trend_fig, use_container_width=True)
        
    with col_chart2:
        # Donut chart for appliance usage
        appliance_fig = plot_appliance_usage(appliance_data)
        st.plotly_chart(appliance_fig, use_container_width=True)
