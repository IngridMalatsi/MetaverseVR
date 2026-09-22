import numpy as np
import plotly.graph_objects as go
import streamlit as st

from dashboard_data import build_model

st.set_page_config(layout="wide")

st.title("Price vs Sales")
df, _ = build_model()

x = df['UnitPrice']
y = df['MarketingBudget']
z = df['UnitsSold']

fig = go.Figure(data=[go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=6,
        color=z,
        colorscale='Turbo',
        opacity=0.9
    ),
    text=[f'Price: R{px}<br>Budget: {by}k<br>Sales: {bz}' for px, by, bz in zip(x, y, z)],
    hovertemplate='%{text}<extra></extra>',
    name='Price and Sales Data'
)])

fig.update_layout(
    title='3D View: Unit Price, Marketing Budget, and Sales',
    scene=dict(
        xaxis_title='Unit Price (R)',
        yaxis_title="Marketing Budget (R'000)",
        zaxis_title='Units Sold',
        camera=dict(eye=dict(x=1.7, y=1.7, z=1.2))
    ),
    height=560,
    margin=dict(l=0, r=0, b=0, t=40),
    template='plotly_dark',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig, use_container_width=True)
