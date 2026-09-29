import streamlit as st
from views import dashboard, prediction, analysis, recommendations, simulator, goals, settings

# Streamlit App Configuration
st.set_page_config(
    page_title="AI Energy Optimizer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    /* Styling for metric cards and containers */
    div[data-testid="stMetricValue"] {
        font-size: 1.8rem;
    }
    div[data-testid="stMetricDelta"] {
        font-size: 1rem;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """
    Main entry point for the AI Energy Optimizer Streamlit application.
    Sets up the sidebar navigation and routes to the selected view.
    """
    st.sidebar.title("⚡ AI Energy Optimizer")
    st.sidebar.markdown("---")
    
    # Navigation mapping
    pages = {
        "📊 Dashboard": dashboard.render,
        "🔮 Prediction": prediction.render,
        "📈 Analysis": analysis.render,
        "💡 Recommendations": recommendations.render,
        "🎛️ Simulator": simulator.render,
        "🎯 Goals & Progress": goals.render,
        "⚙️ Settings / Reports": settings.render
    }
    
    # Radio buttons for navigation
    selection = st.sidebar.radio("Navigation", list(pages.keys()))
    
    st.sidebar.markdown("---")
    st.sidebar.info("ECO Dashboard v1.0.0")
    
    # Render the selected page with error handling
    try:
        pages[selection]()
    except Exception as e:
        st.error(f"An error occurred while loading the page: {e}")

if __name__ == "__main__":
    main()
