import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from dashboard_data import build_model

st.set_page_config(layout="wide")

st.title("Regression Surface")
df, model = build_model()

x_range = np.linspace(df['MarketingBudget'].min(), df['MarketingBudget'].max(), 30)
y_range = np.linspace(df['UnitPrice'].min(), df['UnitPrice'].max(), 30)
xx, yy = np.meshgrid(x_range, y_range)
grid_df = pd.DataFrame(np.c_[xx.ravel(), yy.ravel()], columns=['MarketingBudget', 'UnitPrice'])
zz = model.predict(grid_df).reshape(xx.shape)

fig = go.Figure(data=[go.Surface(
    x=xx,
    y=yy,
    z=zz,
    colorscale='RdBu',
    opacity=0.9,
    showscale=True,
    contours={
        'x': {'show': True, 'start': x_range.min(), 'end': x_range.max(), 'size': 25},
        'y': {'show': True, 'start': y_range.min(), 'end': y_range.max(), 'size': 10},
        'z': {'show': True, 'start': float(zz.min()), 'end': float(zz.max()), 'size': 5}
    }
)])

fig.update_layout(
    title='Predicted Units Sold by Marketing Budget and Unit Price',
    scene=dict(
        xaxis_title="Marketing Budget (R'000)",
        yaxis_title="Unit Price (R)",
        zaxis_title="Units Sold"
    ),
    height=560,
    margin=dict(l=0, r=0, b=0, t=40),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig, use_container_width=True)
