import streamlit as st
import pandas as pd

from api import get_expenses, get_expense, update_expense,delete_expense,get_categories


def show_expenses():

    if "selected_expense" not in st.session_state:
        st.session_state.selected_expense = None

    st.header("Expenses")

#-----------------------------------------
    # create a selectbox to filter the expenses by type and it will send the selected type to the get_expenses function to filter the expenses by type and category for filter in the home page, if not provided, it will return all expenses
    selected_type = st.selectbox(
        "Filter by Type",
        [
            "All",
            "expense",
            "income"
        ]
    )
#---------------------------------------

    # create a selectbox to filter the expenses by category and it will send the selected category to the get_expenses function to filter the expenses by type and category for filter in the home page, if not provided, it will return all expenses
    # selected_category = st.selectbox(
    # "Filter by Category",
    #     [
    #         "All",
    #         "Food",
    #         "Travel",
    #         "Shopping",
    #         "Salary"
    #     ]
    # )

    # we have not used the above hardcoded categories because we want to get the unique categories from the database and show them in the selectbox, so we have created a new endpoint in the backend to get all unique categories and we will use that endpoint to get the categories and show them in the selectbox.
    # so it will dynamically get the unique categories from the database and show them in the selectbox, so that the user can filter the expenses by category and it will send the selected category to the get_expenses function to filter the expenses by type and category for filter in the home page, if not provided, it will return all expenses

    category_response = get_categories()

    categories = ["All"]

    if category_response.status_code == 200:
        categories.extend(category_response.json())

    selected_category = st.selectbox(
        "Filter by Category",
        categories
    )
#---------------------------------------

    # response = get_expenses() # we were doing this before to get all expenses but now we are doing this to filter the expenses by type and category for filter in the home page, if not provided, it will return all expenses
    if selected_type == "All":
        selected_type = None

    if selected_category == "All":
        selected_category = None

    response = get_expenses(
        expense_type=selected_type,
        category=selected_category
    )
#---------------------------------------

    if response.status_code != 200:
        st.error("Unable to fetch expenses.")
        return

    expenses = response.json()

    if not expenses:
        st.info("No expenses found.")
        return

    df = pd.DataFrame(expenses)

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    st.subheader("Update Expense")

    expense_id = st.number_input(
        "Enter Expense ID",
        min_value=1,
        step=1
    )

    if st.button("Load Expense"):

        response = get_expense(expense_id)

        if response.status_code == 200:
            st.session_state.selected_expense = response.json()

        else:
            st.error("Expense not found.")

    # -----------------------------
    # Show update form
    # -----------------------------
    if st.session_state.selected_expense is not None:

        expense = st.session_state.selected_expense

        with st.form("update_expense_form"):

            amount = st.number_input(
                "Amount",
                min_value=0.0,
                value=float(expense["amount"])
            )

            expense_type = st.selectbox(
                "Type",
                ["expense", "income"],
                index=0 if expense["type"] == "expense" else 1
            )

            category = st.text_input(
                "Category",
                value=expense["category"]
            )

            description = st.text_area(
                "Description",
                value=expense["description"] or ""
            )

            expense_date = st.date_input(
                "Expense Date",
                value=pd.to_datetime(expense["expense_date"]).date()
            )

            submitted = st.form_submit_button("Update Expense")

            if submitted:

                updated_expense = {
                    "amount": amount,
                    "type": expense_type,
                    "category": category,
                    "description": description,
                    "expense_date": str(expense_date)
                }

                response = update_expense(
                    expense["id"],
                    updated_expense
                )

                if response.status_code == 200:
                    st.success("Expense updated successfully!")

                    # Hide the form after successful update
                    st.session_state.selected_expense = None

                else:
                    st.error("Unable to update expense.")

    
    # delete the selected expense 
    st.divider()

    st.subheader("Delete Expense")

    delete_expense_id = st.number_input(
        "Enter Expense ID to Delete",
        min_value=1,
        step=1,
        # key="delete_id"  # When two widgets are otherwise identical. like
    )

    if st.button("Delete Expense"):

        response = delete_expense(delete_expense_id)

        if response.status_code == 200:
            st.success("Expense deleted successfully!")

        else:
            st.error("Unable to delete expense.")


# old code where session is not used to store the expense data, instead it fetches the data from the API every time the user wants to update an expense. This is inefficient and can lead to unnecessary API calls.

# def show_expenses():

#     st.header("Expenses")

#     response = get_expenses()

#     if response.status_code != 200:
#         st.error("Unable to fetch expenses.")
#         return

#     expenses = response.json()

#     if not expenses:
#         st.info("No expenses found.")
#         return

#     df = pd.DataFrame(expenses)

#     st.dataframe(
#         df,
#         use_container_width=True
#     )

#     st.divider()

#     st.subheader("Update Expense")

#     expense_id = st.number_input(
#         "Enter Expense ID",
#         min_value=1,
#         step=1
#     )

#     if st.button("Load Expense"):
#         # st.write(expense_id, type(expense_id))

#         response = get_expense(expense_id)

#         if response.status_code == 200:

#             # to check whether data is being fetched correctly
#             # st.success("Expense loaded successfully!")
#             # st.write(response.json()) 

#             expense = response.json()

#             with st.form("update_expense_form"):

#                 amount = st.number_input(
#                     "Amount",
#                     min_value=0.0,
#                     value=float(expense["amount"])
#                 )

#                 expense_type = st.selectbox(
#                     "Type",
#                     ["expense", "income"],
#                     index=0 if expense["type"] == "expense" else 1
#                 )

#                 category = st.text_input(
#                     "Category",
#                     value=expense["category"]
#                 )

#                 description = st.text_area(
#                     "Description",
#                     value=expense["description"] or ""
#                 )

#                 expense_date = st.date_input(
#                     "Expense Date",
#                     value=pd.to_datetime(expense["expense_date"]).date()
#                 )

#                 submitted = st.form_submit_button("Update Expense")

#                 if submitted:

#                     updated_expense = {
#                         "amount": amount,
#                         "type": expense_type,
#                         "category": category,
#                         "description": description,
#                         "expense_date": str(expense_date)
#                     }

#                     response = update_expense(
#                         expense_id,
#                         updated_expense
#                     )

#                     st.write(response.status_code)
#                     st.write(response.text)

#                     if response.status_code == 200:
#                         st.success("Expense updated successfully!")

#                     else:
#                         st.error("Unable to update expense.")
                    

#         else:
#             st.error("Expense not found.")