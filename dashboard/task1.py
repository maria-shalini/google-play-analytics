import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import pytz
import streamlit as st

def is_time_allowed(start_hour, end_hour):
    ist = pytz.timezone("Asia/Kolkata")
    current_hour = datetime.now(ist).hour
    return start_hour <= current_hour < end_hour

def task1_grouped_bar_chart():

    if not is_time_allowed(15, 17):
        return None

    df = pd.read_csv("data/cleaned_apps.csv")
    df["Last Updated"] = pd.to_datetime(df["Last Updated"], errors="coerce")

    filtered_df = df[
        (df["Rating"] >= 4.0) &
        (df["Size_MB"] < 10) &
        (df["Last Updated"].dt.month == 1)
    ]

    if filtered_df.empty:
        return None

    top_categories = (
        filtered_df.groupby("Category")["Installs"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .index
    )

    final_df = filtered_df[filtered_df["Category"].isin(top_categories)]

    summary_df = final_df.groupby("Category").agg(
        Average_Rating=("Rating", "mean"),
        Total_Reviews=("Reviews", "sum")
    ).sort_values(by="Average_Rating", ascending=False)

    fig, ax = plt.subplots(figsize=(12, 6))
    summary_df.plot(kind="bar", ax=ax)

    ax.set_title(
        "Average Rating vs Total Reviews\nTop 10 App Categories by Installs"
    )
    ax.set_xlabel("App Category")
    ax.set_ylabel("Value")
    ax.legend(["Average Rating", "Total Reviews"])
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    st.pyplot(fig)
    return fig
