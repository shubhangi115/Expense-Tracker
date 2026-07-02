import streamlit as st
from streamlit_option_menu import option_menu

from views.home import show_home
from views.add_expense import show_add_expense
from views.expense import show_expenses
from views.analytics import show_analytics

st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="wide"
)

st.title("Expense Tracker")
st.caption("Personal Finance Dashboard")

selected = option_menu(
    menu_title=None,
    options=[
        "Home",
        "Add Expense",
        "View Expenses",
        "Analytics"
    ],
    icons=[
        "house",
        "plus-circle",
        "table",
        "bar-chart"
    ],
    orientation="horizontal"
)

st.divider()

if selected == "Home":
    show_home()

elif selected == "Add Expense":
    show_add_expense()

elif selected == "View Expenses":
    show_expenses()

elif selected == "Analytics":
    show_analytics()





# import streamlit as st

# st.set_page_config(
#     page_title="Expense Tracker",
#     page_icon="💰",
#     layout="wide"
# )

# st.title(" Expense Tracker")

# st.markdown("""
# Welcome to the Expense Tracker application.

# This application allows you to:

# -  Add Expenses
# -  View Expenses
# -  Update Expenses
# -  View Analytics

# Use the navigation menu on the left to get started.
# """)






# import streamlit as st
# from streamlit_option_menu import option_menu

# st.set_page_config(
#     page_title="Expense Tracker",
#     page_icon="💰",
#     layout="wide"
# )

# # -------------------------
# # Header
# # -------------------------

# st.title("Expense Tracker")
# st.caption("Personal Finance Dashboard")

# # -------------------------
# # Navigation
# # -------------------------

# selected = option_menu(
#     menu_title=None,
#     options=[
#         "Home",
#         "Add Expense",
#         "View Expenses",
#         "Analytics"
#     ],
#     icons=[
#         "house",
#         "plus-circle",
#         "table",
#         "bar-chart"
#     ],
#     orientation="horizontal"
# )

# st.divider()


# if selected == "Home":

#     st.header("Hey , Welcome Back ")

#     st.write(
#         "Manage your personal expenses efficiently."
#     )

# elif selected == "Add Expense":

#     st.header("Add Expense")

# elif selected == "View Expenses":

#     st.header("View Expenses")

# elif selected == "Analytics":

#     st.header("Analytics")

# if selected == "Home":

#     st.header("Dashboard")

#     col1, col2, col3, col4 = st.columns(4)

#     with col1:
#         st.metric(
#             "💵 Income",
#             "₹0"
#         )

#     with col2:
#         st.metric(
#             "💸 Expense",
#             "₹0"
#         )

#     with col3:
#         st.metric(
#             "💰 Balance",
#             "₹0"
#         )

#     with col4:
#         st.metric(
#             "🧾 Transactions",
#             "0"
#         )

    

#     st.divider()

#     st.subheader("Recent Transactions")

#     st.info("No transactions yet.")

