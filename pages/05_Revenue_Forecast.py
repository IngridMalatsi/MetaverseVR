import plotly.graph_objects as go
import streamlit as st

from dashboard_data import build_model

st.set_page_config(layout="wide")

st.title("Revenue Forecast")
df, _ = build_model()

df['Revenue'] = df['UnitsSold'] * df['UnitPrice']

fig = go.Figure(data=[go.Scatter3d(
    x=df['MarketingBudget'],
    y=df['UnitPrice'],
    z=df['Revenue'],
    mode='markers',
    marker=dict(
        size=7,
        color=df['Revenue'],
        colorscale='Plasma',
        opacity=0.9
    ),
    text=[f'Budget: {bx}k<br>Price: R{by}<br>Revenue: R{bz:,.2f}' for bx, by, bz in zip(df['MarketingBudget'], df['UnitPrice'], df['Revenue'])],
    hovertemplate='%{text}<extra></extra>',
    name='Revenue Data'
)])

fig.update_layout(
    title='3D View: Marketing Budget, Unit Price, and Revenue',
    scene=dict(
        xaxis_title="Marketing Budget (R'000)",
        yaxis_title='Unit Price (R)',
        zaxis_title='Revenue (R)',
        camera=dict(eye=dict(x=1.7, y=1.7, z=1.2))
    ),
    height=560,
    margin=dict(l=0, r=0, b=0, t=40),
    template='plotly_dark',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig, use_container_width=True)
