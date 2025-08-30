import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def process_data(df):
    results = {}

    if "origin" in df.columns and "destination" in df.columns:
        df["route"] = df["origin"] + "-" + df["destination"]
        popular_routes = df["route"].value_counts().head(10)
        results["popular_routes"] = popular_routes

    if "price" in df.columns and "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        price_trends = df.groupby(df["date"].dt.to_period("M"))["price"].mean()
        results["price_trends"] = price_trends

        monthly_demand = df.groupby(df["date"].dt.to_period("M")).size()
        results["monthly_demand"] = monthly_demand

    return results
