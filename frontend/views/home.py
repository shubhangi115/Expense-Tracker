import streamlit as st
from api import get_summary, get_expenses


def show_home():

    st.header("Hey, Welcome Back ")

# to get the expense,income,transation etc in the home live 
#---------------------------------------------------------
    response = get_summary()

    if response.status_code != 200:
        st.error("Unable to load dashboard.")
        return

    summary = response.json()

    income = 0
    expense = 0

    income_transactions = 0
    expense_transactions = 0

    for item in summary:

        if item["type"] == "income":
            income = item["total_amount"]
            income_transactions = item["total_transactions"]

        elif item["type"] == "expense":
            expense = item["total_amount"]
            expense_transactions = item["total_transactions"]
    
    # for balance calculation
    balance = income - expense

    # for total transactions calculation
    total_transactions = (
        income_transactions +
        expense_transactions
    )
#------------------------------------------------------------------------

    st.write(
        "Manage your personal expenses efficiently."
    )

    st.header("Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("💵 Income", f"₹{income:,.2f}")

    with col2:
        st.metric("💸 Expense", f"₹{expense:,.2f}")

    with col3:
        st.metric("💰 Balance", f"₹{balance:,.2f}")

    with col4:
        st.metric("🧾 Transactions", f"{total_transactions}")

    st.divider()

    st.subheader("Recent Transactions")

    st.info("No transactions yet.")
    # to add recent 5 transactions in the home page instead of showing no transactions yet
   
