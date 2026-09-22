import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from dashboard_data import build_model

st.set_page_config(layout="wide")

st.title("3D Sales Forecast")
df, model = build_model()

input_budget = st.sidebar.slider("Marketing Budget (R'000)", float(df['MarketingBudget'].min()), float(df['MarketingBudget'].max()), 250.0, step=5.0)
input_price = st.sidebar.slider("Unit Price (R)", float(df['UnitPrice'].min()), float(df['UnitPrice'].max()), 85.0, step=1.0)

input_data = pd.DataFrame([[input_budget, input_price]], columns=['MarketingBudget', 'UnitPrice'])
predicted_units = model.predict(input_data)[0]

fig = go.Figure()
fig.add_trace(go.Scatter3d(
    x=df['MarketingBudget'],
    y=df['UnitPrice'],
    z=df['UnitsSold'],
    mode='markers',
    marker=dict(size=4, color=df['UnitsSold'], colorscale='Viridis', opacity=0.75),
    name='Historical Data'
))
fig.add_trace(go.Scatter3d(
    x=[input_budget],
    y=[input_price],
    z=[predicted_units],
    mode='markers+text',
    marker=dict(size=10, color='red', symbol='diamond'),
    text=['Forecast Output'],
    textposition='top center',
    name='Current Target Point'
))

x_range = np.linspace(df['MarketingBudget'].min(), df['MarketingBudget'].max(), 12)
y_range = np.linspace(df['UnitPrice'].min(), df['UnitPrice'].max(), 12)
xx, yy = np.meshgrid(x_range, y_range)
grid_df = pd.DataFrame(np.c_[xx.ravel(), yy.ravel()], columns=['MarketingBudget', 'UnitPrice'])
zz = model.predict(grid_df).reshape(xx.shape)

fig.add_trace(go.Surface(
    x=xx,
    y=yy,
    z=zz,
    colorscale='Blues',
    opacity=0.35,
    showscale=False,
    name='Predictive Surface'
))

fig.update_layout(
    scene=dict(
        xaxis_title="Marketing Budget (R'000)",
        yaxis_title="Unit Price (R)",
        zaxis_title="Units Sold",
        camera=dict(eye=dict(x=1.6, y=1.6, z=1.2))
    ),
    height=560,
    margin=dict(l=0, r=0, b=0, t=30),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig, use_container_width=True)
