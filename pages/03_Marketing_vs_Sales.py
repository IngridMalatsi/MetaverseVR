import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from dashboard_data import build_model

st.set_page_config(layout="wide")

st.title("Marketing vs Sales")
df, _ = build_model()

x = df['MarketingBudget']
y = df['UnitPrice']
z = df['UnitsSold']

fig = go.Figure(data=[go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=6,
        color=z,
        colorscale='Cividis',
        opacity=0.9,
        symbol='circle'
    ),
    text=[f'Budget: {bx}k<br>Price: R{by}<br>Sales: {bz}' for bx, by, bz in zip(x, y, z)],
    hovertemplate='%{text}<extra></extra>',
    name='Marketing and Sales Data'
)])

fig.update_layout(
    title='3D View: Marketing Budget, Price, and Units Sold',
    scene=dict(
        xaxis_title="Marketing Budget (R'000)",
        yaxis_title='Unit Price (R)',
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
