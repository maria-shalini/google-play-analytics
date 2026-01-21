import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import pytz
import streamlit as st


def is_time_allowed(start_hour, end_hour):
    ist = pytz.timezone("Asia/Kolkata")
    current_hour = datetime.now(ist).hour
    return start_hour <= current_hour < end_hour


def task1_grouped_bar_chart(test_mode=False):

    # ⏰ Time restriction
    if not test_mode and not is_time_allowed(15, 17):
        return None

    df = pd.read_csv("data/cleaned_apps.csv")
    df["Last Updated"] = pd.to_datetime(df["Last Updated"], errors="coerce")

    # 🎛 INTERACTIVE FILTERS (Sidebar)
    st.sidebar.header("Task 1 Filters")

    min_rating = st.sidebar.slider(
        "Minimum Average Rating",
        min_value=4.0,
        max_value=5.0,
        value=4.0,
        step=0.1
    )

    max_size = st.sidebar.slider(
        "Maximum App Size (MB)",
        min_value=1,
        max_value=50,
        value=10
    )

    # Base filtering
    filtered_df = df[
        (df["Rating"] >= min_rating) &
        (df["Size_MB"] <= max_size) &
        (df["Last Updated"].dt.month == 1)
    ]

    if filtered_df.empty:
        st.info("No data available for selected filters.")
        return None

    # Top 10 categories by installs
    top_categories = (
        filtered_df.groupby("Category")["Installs"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .index
    )

    category_selection = st.sidebar.multiselect(
        "Select App Categories",
        options=top_categories,
        default=list(top_categories)
    )

    final_df = filtered_df[filtered_df["Category"].isin(category_selection)]

    if final_df.empty:
        st.warning("Please select at least one category.")
        return None

    summary_df = final_df.groupby("Category").agg(
        Average_Rating=("Rating", "mean"),
        Total_Reviews=("Reviews", "sum")
    )

    # 📊 Plot
    fig, ax = plt.subplots(figsize=(12, 6))
    summary_df.plot(kind="bar", ax=ax)

    ax.set_title("Average Rating vs Total Reviews (Top Categories)")
    ax.set_xlabel("App Category")
    ax.set_ylabel("Value")
    ax.legend(["Average Rating", "Total Reviews"])
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    st.pyplot(fig)
    return fig
