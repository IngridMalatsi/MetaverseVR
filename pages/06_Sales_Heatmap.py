import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from dashboard_data import build_model

st.set_page_config(layout="wide")

st.title("Sales Heatmap")
df, _ = build_model()

x = np.linspace(df['MarketingBudget'].min(), df['MarketingBudget'].max(), 30)
y = np.linspace(df['UnitPrice'].min(), df['UnitPrice'].max(), 30)
xx, yy = np.meshgrid(x, y)

grid = pd.DataFrame({'MarketingBudget': xx.ravel(), 'UnitPrice': yy.ravel()})
# approximate surface from the original data using a simple interpolation-based lookup
z = np.array([
    df[(df['MarketingBudget'].sub(mb).abs() < 10) & (df['UnitPrice'].sub(up).abs() < 10)]['UnitsSold'].mean()
    for mb, up in zip(grid['MarketingBudget'], grid['UnitPrice'])
])

z = np.nan_to_num(z, nan=0).reshape(xx.shape)

fig = go.Figure(data=[go.Surface(
    x=xx,
    y=yy,
    z=z,
    colorscale='Viridis',
    opacity=0.95,
    contours={
        'x': {'show': True, 'start': x.min(), 'end': x.max(), 'size': 20},
        'y': {'show': True, 'start': y.min(), 'end': y.max(), 'size': 10},
        'z': {'show': True, 'start': float(z.min()), 'end': float(z.max()), 'size': 10}
    },
    hovertemplate='Marketing Budget: %{x}<br>Unit Price: %{y}<br>Units Sold: %{z}<extra></extra>'
)])

fig.update_layout(
    title='3D Sales Surface by Marketing Budget and Unit Price',
    scene=dict(
        xaxis_title="Marketing Budget (R'000)",
        yaxis_title='Unit Price (R)',
        zaxis_title='Units Sold',
        camera=dict(eye=dict(x=1.5, y=1.5, z=1.2))
    ),
    height=560,
    template='plotly_dark',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig, use_container_width=True)
