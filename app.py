import streamlit as st
import pandas as pd
import altair as alt
import os

from utils.data_processing import load_data, process_data

st.set_page_config(page_title="Airline Market Demand", layout="wide")

st.title("✈️ Airline Booking Market Demand Dashboard")

st.sidebar.header("Upload or Use Sample Data")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type="csv")
use_sample = st.sidebar.checkbox("Use Sample Data", value=True)

if use_sample:
    data_path = os.path.join("data", "sample_data.csv")
    df = load_data(data_path)
elif uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    st.warning("Please upload a file or use the sample dataset.")
    st.stop()

st.subheader("Raw Data Preview")
st.dataframe(df.head())

processed = process_data(df)

st.subheader("Insights")

# Popular routes
st.markdown("### Top 10 Popular Routes")
st.bar_chart(processed["popular_routes"])

# Price trends
st.markdown("### Average Price by Month")
st.line_chart(processed["price_trends"])

# Demand trends
st.markdown("### Demand by Month")
st.line_chart(processed["monthly_demand"])
