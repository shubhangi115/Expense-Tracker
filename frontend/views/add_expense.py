import streamlit as st
from datetime import date
from api import create_expense


def show_add_expense():

    st.header("Add Expense")

    st.write("Fill in the details below.")

    with st.form("expense_form"):

        amount = st.number_input(
            "Amount",
            min_value=0,
            step=1
        )

        expense_type = st.selectbox(
            "Type",
            ["expense", "income"]
        )

        category = st.text_input(
            "Category"
        )

        description = st.text_area(
            "Description"
        )

        expense_date = st.date_input(
            "Expense Date",
            value=date.today()
        )

        submitted = st.form_submit_button(
            "Save Expense"
        )

        if submitted:

            expense_data = {
                "amount": amount,
                "type": expense_type,
                "category": category,
                "description": description,
                "expense_date": str(expense_date)
            }

            response = create_expense(expense_data)
            
            # but the post should return a 201 status code for created, not 200
            
            # if response.status_code == 200:
            if response.status_code == 201:
                st.success("Expense added successfully!")

            else:
                st.error(response.json()["detail"])