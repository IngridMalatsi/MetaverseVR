import streamlit as st
from dashboard_data import build_model

st.set_page_config(
    page_title="Overview",
    page_icon="📊",
    layout="wide"
)

st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #f4f1ea 0%, #ece7df 100%);
        color: #1f2933;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
    }

    [data-testid="stSidebar"] * {
        color: #f8fafc !important;
    }

    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 1500px;
    }

    h1, h2, h3, h4, h5 {
        color: #12263a;
        font-weight: 700;
    }

    .stMetric {
        background: rgba(255,255,255,0.55);
        border: 1px solid rgba(18,38,58,0.12);
        border-radius: 12px;
        padding: 0.8rem;
        box-shadow: 0 2px 10px rgba(15,23,42,0.06);
    }

    .stAlert, .stInfo {
        background: rgba(255,255,255,0.56);
        border: 1px solid rgba(18,38,58,0.12);
        color: #1f2933;
    }

    .stPlotlyChart > div {
        border-radius: 12px;
        box-shadow: 0 4px 18px rgba(15,23,42,0.08);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("VR Data Analytics Learning Environment")
st.caption("An immersive analytics dashboard for teaching data-driven learning through interactive, 3D visual exploration.")

st.markdown("### Project objectives")
st.markdown(
    """
    1. To develop a Virtual Reality (VR) learning environment for data analytics education.  
    2. To enable students to interact with large datasets through immersive three-dimensional (3D) visualisations.  
    3. To improve students' understanding of statistical analysis and machine learning concepts through real-time simulations.  
    4. To provide a practical environment where students can explore predictive analytics models and assess their outcomes.  
    5. To enhance student engagement and participation through interactive, data-driven learning activities.
    """
)

# Shared summary data

df, _ = build_model()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Avg Units Sold", f"{df['UnitsSold'].mean():,.1f} units")
with col2:
    st.metric("Budget Range", f"R{df['MarketingBudget'].min():,.0f}k - R{df['MarketingBudget'].max():,.0f}k")
with col3:
    st.metric("Price Range", f"R{df['UnitPrice'].min():,.0f} - R{df['UnitPrice'].max():,.0f}")

st.markdown("---")

st.subheader("Available learning views")
st.markdown(
    """
    - 3D Sales Forecast
    - Regression Surface
    - Marketing vs Sales
    - Price vs Sales
    - Revenue Forecast
    - Sales Heatmap
    """
)

st.info("Each chart now lives on its own dedicated page in the left sidebar so students can compare patterns, predictions, and business scenarios in a structured learning flow.")