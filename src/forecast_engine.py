import pandas as pd
from prophet import Prophet


def sales_forecast(df):

    df["Date"] = pd.to_datetime(df["Date"])

    monthly = df.groupby(df["Date"].dt.to_period("M"))["Revenue"].sum().reset_index()

    monthly["Date"] = monthly["Date"].dt.to_timestamp()

    forecast_df = monthly.rename(columns={"Date": "ds", "Revenue": "y"})

    model = Prophet()

    model.fit(forecast_df)

    future = model.make_future_dataframe(periods=6, freq="M")

    forecast = model.predict(future)

    return forecast