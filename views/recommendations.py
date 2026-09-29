import streamlit as st
from utils.recommendations_engine import get_recommendations, calculate_carbon_footprint

def render():
    """
    Renders the Smart Recommendations page with AI-driven tips
    and a carbon footprint calculator.
    """
    st.title("💡 Smart Recommendations")
    st.markdown("Actionable AI-driven insights to help you reduce consumption and save money.")
    
    # Mock parameters
    current_usage = 12.5 # kWh
    peak_ratio = 0.45
    
    tips = get_recommendations(current_usage, peak_ratio)
    
    st.subheader("Personalized Tips")
    
    for tip in tips:
        if tip["type"] == "warning":
            st.warning(f"**{tip['category']} (Impact: {tip['impact']})**\n\n{tip['text']}")
        elif tip["type"] == "info":
            st.info(f"**{tip['category']} (Impact: {tip['impact']})**\n\n{tip['text']}")
        else:
            st.success(f"**{tip['category']} (Impact: {tip['impact']})**\n\n{tip['text']}")
            
    st.markdown("---")
    
    st.subheader("🌍 Environmental Impact")
    st.markdown("See how your energy savings contribute to a greener planet.")
    
    # Simple interactive carbon footprint calculator
    saved_kwh_input = st.number_input("Enter your goal for monthly kWh savings:", min_value=0.0, value=25.0, step=1.0)
    
    co2_saved = calculate_carbon_footprint(saved_kwh_input)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Target Energy Savings", value=f"{saved_kwh_input} kWh")
    with col2:
        st.metric(label="Estimated CO₂ Emission Reduced", value=f"{co2_saved:.2f} kg", delta="Greener footprint!")
        
    st.info("💡 Did you know? Saving 25 kWh is equivalent to the carbon absorbed by a tree over several months!")
