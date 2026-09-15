# MetaverseVR

VR Powered Predictive Analytics Lab for executive-level business forecasting and interactive data exploration.

This project combines a lightweight machine learning model with a modern visual dashboard to help users simulate how marketing spend and pricing decisions affect expected sales performance.

## Overview

MetaverseVR is a Streamlit application that:

- Generates synthetic historical business data
- Trains a linear regression model to forecast sales volume
- Lets users adjust marketing budget and unit price in real time
- Displays a 3D predictive surface for business scenario analysis
- Shows projected units sold and gross revenue instantly

## Key Features

- Interactive sidebar controls for business simulation
- Real-time sales forecast based on pricing and marketing inputs
- 3D scatter and surface visualization using Plotly
- Dark-themed executive dashboard styling
- Lightweight data science workflow using scikit-learn

## Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- scikit-learn

## Project Structure

- `app.py` — main dashboard and forecasting logic
- `README.md` — project documentation

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Install dependencies

```bash
pip install streamlit numpy pandas plotly scikit-learn
```

### Run the app

```bash
streamlit run app.py
```

Then open the local URL displayed in the terminal, typically:

```text
http://localhost:8501
```

## How It Works

1. The app generates example business data with variables for:
   - Marketing budget
   - Unit price
   - Units sold
2. A `LinearRegression` model is trained on this data.
3. The user adjusts the marketing budget and unit price using sliders.
4. The model predicts sales volume and revenue in real time.
5. The result is displayed as a 3D visual forecast surface and summary metrics.

## Use Case

This dashboard is designed for business planning and scenario analysis, especially for teams exploring the relationship between:

- marketing investment
- product pricing
- expected sales outcomes
- projected revenue

## Notes

The app uses synthetic data for demonstration purposes and is intended as a prototype for predictive analytics dashboards and VR-inspired business visualization.
