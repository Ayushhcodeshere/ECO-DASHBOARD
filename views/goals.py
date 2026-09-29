import streamlit as st

def render():
    """
    Renders the Goals & Progress tracking page to monitor budget
    and energy consumption targets.
    """
    st.title("🎯 Goals & Progress")
    st.markdown("Set targets for your energy consumption and track your monthly progress.")
    
    # Mock goals
    monthly_budget = 1000 # ₹
    current_spent = 850
    
    monthly_kwh_target = 180
    current_kwh = 152.6
    
    st.subheader("Monthly Tracker")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Budget Progress")
        budget_pct = min(100, int((current_spent / monthly_budget) * 100))
        st.progress(budget_pct / 100)
        st.write(f"**₹{current_spent}** used out of **₹{monthly_budget}** ({budget_pct}%)")
        if budget_pct > 90:
            st.error("Warning: You are approaching your monthly budget limit!")
        else:
            st.success("You are on track to stay within your budget.")
            
    with col2:
        st.markdown("### Energy Consumption Progress")
        kwh_pct = min(100, int((current_kwh / monthly_kwh_target) * 100))
        st.progress(kwh_pct / 100)
        st.write(f"**{current_kwh:.1f} kWh** used out of **{monthly_kwh_target} kWh** ({kwh_pct}%)")
        if kwh_pct > 90:
            st.error("Warning: You are approaching your monthly energy limit!")
        else:
            st.success("You are efficiently managing your energy.")
            
    st.markdown("---")
    
    st.subheader("Adjust Your Goals")
    
    new_budget = st.number_input("Update Monthly Budget (₹):", min_value=100, value=monthly_budget, step=50)
    new_target = st.number_input("Update Monthly Energy Target (kWh):", min_value=50, value=monthly_kwh_target, step=10)
    
    if st.button("Save New Goals"):
        st.success("Goals updated successfully! (Note: This is a demo, values won't persist across sessions without a database).")
