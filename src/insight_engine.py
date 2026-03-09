import pandas as pd


def load_data():

    df = pd.read_csv("data/raw/sales_data.csv")

    df["Date"] = pd.to_datetime(df["Date"])

    return df


def total_revenue(df):

    revenue = df["Revenue"].sum()

    return f"Total revenue generated: ${revenue:,.0f}"


def top_category(df):

    category = df.groupby("Category")["Revenue"].sum().idxmax()

    return f"Top revenue category: {category}"


def top_region(df):

    region = df.groupby("Region")["Revenue"].sum().idxmax()

    return f"Best performing region: {region}"


def top_product(df):

    product = df.groupby("Product")["Units"].sum().idxmax()

    return f"Most sold product: {product}"


def sales_trend(df):

    monthly = df.groupby(df["Date"].dt.to_period("M"))["Revenue"].sum()

    growth = monthly.pct_change().mean() * 100

    return f"Average monthly growth: {growth:.2f}%"


def generate_insights():

    df = load_data()

    insights = [
        total_revenue(df),
        top_category(df),
        top_region(df),
        top_product(df),
        sales_trend(df)
    ]

    return insights