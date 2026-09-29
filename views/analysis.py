import streamlit as st
from utils.data_gen import get_hourly_consumption_data
from utils.charts import plot_peak_hours

def render():
    """
    Renders the Detailed Analysis page, focusing on peak usage hours
    and anomaly detection events.
    """
    st.title("📈 Detailed Analysis")
    st.markdown("Analyze usage patterns, peak hours, and detect anomalies.")
    
    st.subheader("Peak Usage Hours Analysis")
    
    hourly_data = get_hourly_consumption_data(days=30) # get a month of data for solid average
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        fig = plot_peak_hours(hourly_data)
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.markdown("### Peak Hours Summary")
        st.info("Peak Hours: **12 PM - 4 PM**")
        st.warning("Consumption is typically **45% higher** during these hours.")
        
        st.markdown("### Cost Implications")
        st.write("Using heavy appliances during peak hours incurs higher tariff rates. Try to shift usage to off-peak hours (before 12 PM or after 8 PM) to save up to 20% on your monthly bill.")
        
    st.markdown("---")
    
    st.subheader("Anomaly Detection Deep Dive")
    
    st.write("Our AI models continuously monitor your usage to detect unusual spikes.")
    
    # Mocking some anomaly data
    anomaly_dates = [
        {"date": "2026-08-14 14:00", "expected": 1.2, "actual": 2.5, "reason": "Unusual AC Usage"},
        {"date": "2026-08-10 18:00", "expected": 0.8, "actual": 1.9, "reason": "Heavy Appliance Run (Washer/Dryer)"},
        {"date": "2026-08-02 22:00", "expected": 0.4, "actual": 1.5, "reason": "Unknown (Review Needed)"}
    ]
    
    for anomaly in anomaly_dates:
        with st.expander(f"⚠️ Spike Detected on {anomaly['date']} - {anomaly['reason']}"):
            col_a, col_b = st.columns(2)
            col_a.metric("Expected Usage", f"{anomaly['expected']} kWh")
            col_b.metric("Actual Usage", f"{anomaly['actual']} kWh", delta=f"{anomaly['actual'] - anomaly['expected']:.1f} kWh", delta_color="inverse")
            if "Unknown" in anomaly["reason"]:
                st.button(f"Investigate incident on {anomaly['date']}")
