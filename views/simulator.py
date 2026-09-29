import streamlit as st

def render():
    """
    Renders the What-If Simulator page for users to experiment with
    different usage scenarios and see their cost impact.
    """
    st.title("🎛️ What-If Simulator")
    st.markdown("Experiment with different usage scenarios to see how they impact your consumption and bill.")
    
    # Base assumptions
    base_ac_hours = 8
    base_tv_hours = 4
    ac_kwh_per_hour = 1.5 # example rate
    tv_kwh_per_hour = 0.2
    cost_per_kwh = 8.0 # ₹8 per kWh
    
    base_daily_kwh = 12.0 # baseline other usage + AC + TV
    base_monthly_bill = (base_daily_kwh * 30) * cost_per_kwh
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Adjust Usage Parameters")
        
        ac_slider = st.slider("AC Usage (Hours/Day)", min_value=0, max_value=24, value=base_ac_hours, step=1)
        tv_slider = st.slider("TV / Appliance Usage (Hours/Day)", min_value=0, max_value=24, value=base_tv_hours, step=1)
        
        st.info("Tip: Reducing AC usage by just 1 hour a day can save up to 10% on your monthly bill.")
        
    with col2:
        st.subheader("Simulation Results")
        
        # Calculate new usage
        ac_diff = ac_slider - base_ac_hours
        tv_diff = tv_slider - base_tv_hours
        
        daily_kwh_diff = (ac_diff * ac_kwh_per_hour) + (tv_diff * tv_kwh_per_hour)
        new_daily_kwh = base_daily_kwh + daily_kwh_diff
        
        new_monthly_bill = (new_daily_kwh * 30) * cost_per_kwh
        savings = base_monthly_bill - new_monthly_bill
        savings_kwh = (base_daily_kwh - new_daily_kwh) * 30
        
        st.metric(label="Simulated Daily Usage", value=f"{new_daily_kwh:.2f} kWh", 
                  delta=f"{daily_kwh_diff:.2f} kWh vs current", delta_color="inverse")
                  
        st.metric(label="Estimated Monthly Bill", value=f"₹{new_monthly_bill:.0f}", 
                  delta=f"₹{-savings:.0f} vs current", delta_color="inverse")
                  
        if savings > 0:
            st.success(f"🎉 Great job! You could save **₹{savings:.0f}** ({savings_kwh:.1f} kWh) per month with these changes.")
        elif savings < 0:
            st.warning(f"⚠️ This scenario increases your monthly bill by **₹{-savings:.0f}**.")
        else:
            st.info("No change from current baseline.")
