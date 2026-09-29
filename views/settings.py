import streamlit as st
import pandas as pd
from io import BytesIO

def render():
    """
    Renders the Settings & Reports page allowing data export,
    API integration testing, and preference configuration.
    """
    st.title("⚙️ Settings & Reports")
    st.markdown("Configure your dashboard and export data reports.")
    
    tabs = st.tabs(["Data Export", "API & Integration", "Preferences"])
    
    with tabs[0]:
        st.subheader("Export Usage Data")
        st.write("Download your historical consumption and predictions as a CSV report.")
        
        # Mock data for export
        export_df = pd.DataFrame({
            "Date": ["2026-08-01", "2026-08-02", "2026-08-03"],
            "Actual_kWh": [12.5, 11.2, 13.0],
            "Predicted_kWh": [12.0, 11.5, 12.8],
            "Cost_INR": [100.0, 89.6, 104.0]
        })
        
        csv = export_df.to_csv(index=False).encode('utf-8')
        
        st.download_button(
            label="Download Monthly CSV Report",
            data=csv,
            file_name='energy_report_aug_2026.csv',
            mime='text/csv',
        )
        
    with tabs[1]:
        st.subheader("Smart Meter Integration")
        st.write("Configure connection to your IoT smart meter or energy provider API.")
        
        st.text_input("API Key", type="password", value="demo-key-12345")
        st.text_input("Meter ID", value="MTR-998877")
        
        if st.button("Test Connection"):
            st.success("Connection to Smart Meter successful! Data is syncing...")
            
    with tabs[2]:
        st.subheader("UI Preferences")
        st.write("Theming is generally handled by Streamlit's native settings (top right menu), but you can set specific app preferences here.")
        
        st.selectbox("Currency Display", ["INR (₹)", "USD ($)", "EUR (€)"])
        st.selectbox("Energy Unit", ["kWh", "Wh", "MJ"])
        st.checkbox("Enable Push Notifications for High Usage", value=True)
        st.checkbox("Enable Weekly Email Reports", value=False)
        
        if st.button("Save Preferences"):
            st.toast("Preferences saved successfully!", icon="✅")
