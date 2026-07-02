import streamlit as st
import pandas as pd
import plotly.express as px

from api import (
    get_summary,
    get_category_summary,
    get_monthly_summary
)


def show_analytics():

    st.header("Expense Analytics")

    green_palette = [
        "#9F46B5",  # Teal Green
        "#72A1C5",  # Forest Green
        "#EA9595",  # Green
        "#7CB342",  # Lime Green
        "#DCE1A5"   # Pale Green
    ]

    # ------------------------
    # Overall Summary
    # ------------------------
    response = get_summary()

    if response.status_code != 200:
        st.error("Unable to load summary.")
        return

    summary = pd.DataFrame(response.json())

    total_amount = summary["total_amount"].sum()
    total_transactions = summary["total_transactions"].sum()
    average_amount = summary["average_amount"].mean()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Expense", f"₹{total_amount:.2f}")

    with col2:
        st.metric("Transactions", int(total_transactions))

    with col3:
        st.metric("Average Expense", f"₹{average_amount:.2f}")

    st.divider()

    # ------------------------
    # Category Summary
    # ------------------------
    response = get_category_summary()

    if response.status_code == 200:

        category_df = pd.DataFrame(response.json())

        st.subheader("Expenses by Category")

        pie_fig = px.pie(
            category_df,
            names="category",
            values="total_amount",
            hole=0.4,
            color="category",
            color_discrete_sequence=green_palette
        )

        st.plotly_chart(
            pie_fig,
            width="stretch"
        )

        bar_fig = px.bar(
            category_df,
            x="category",
            y="total_amount",
            color="category",
            color_discrete_sequence=green_palette
        )

        st.plotly_chart(
            bar_fig,
            width="stretch"
        )

    st.divider()

    # ------------------------
    # Monthly Summary
    # ------------------------
    response = get_monthly_summary()

    if response.status_code == 200:

        monthly_df = pd.DataFrame(response.json())

        st.subheader("Monthly Expenses")

        line_fig = px.line(
            monthly_df,
            x="month",
            y="total_amount",
            markers=True,
            color_discrete_sequence=["#2E7D32"]
        )

        st.plotly_chart(
            line_fig,
            width="stretch"
        )