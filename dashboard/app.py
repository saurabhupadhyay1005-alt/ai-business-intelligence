import streamlit as st
import pandas as pd
import plotly.express as px

from src.insight_engine import generate_insights
from src.forecast_engine import sales_forecast


st.set_page_config(page_title="AI Business Intelligence Dashboard", layout="wide")

st.title("AI Business Intelligence Dashboard")

st.write("Upload a sales dataset to analyze business performance and forecast future revenue.")


uploaded_file = st.file_uploader("Upload sales dataset (CSV)", type="csv")


if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())


    st.subheader("Revenue by Category")

    category = df.groupby("Category")["Revenue"].sum().reset_index()

    fig1 = px.bar(category, x="Category", y="Revenue", color="Category")

    st.plotly_chart(fig1, use_container_width=True)


    st.subheader("Revenue by Region")

    region = df.groupby("Region")["Revenue"].sum().reset_index()

    fig2 = px.pie(region, names="Region", values="Revenue")

    st.plotly_chart(fig2, use_container_width=True)


    st.subheader("AI Business Insights")

    insights = generate_insights()

    for insight in insights:
        st.write("•", insight)


    st.subheader("AI Revenue Forecast")

    forecast = sales_forecast(df)

    fig3 = px.line(forecast, x="ds", y="yhat", title="Predicted Revenue")

    st.plotly_chart(fig3, use_container_width=True)