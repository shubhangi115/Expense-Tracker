import requests

BASE_URL = "http://127.0.0.1:8000"

# CRUD operations for expenses

# Create a new expense
def create_expense(expense_data: dict):

    response = requests.post(
        f"{BASE_URL}/expenses",
        json=expense_data
    )

    return response

# Get all expenses
def get_expenses(
    expense_type=None,
    category=None
):

    params = {}

    if expense_type:
        params["expense_type"] = expense_type

    if category:
        params["category"] = category

    response = requests.get(
        f"{BASE_URL}/expenses",
        params=params
    )

    return response

# Get a single expense by ID
def update_expense(expense_id: int, expense_data: dict):

    response = requests.put(
        f"{BASE_URL}/expenses/{expense_id}",
        json=expense_data
    )

    return response

# Get a single expense by ID
def get_expense(expense_id: int):

    response = requests.get(
        f"{BASE_URL}/expenses/{expense_id}"
    )

    return response 


# delete a single expense by ID
def delete_expense(expense_id: int):

    response = requests.delete(
        f"{BASE_URL}/expenses/{expense_id}"
    )

    return response

# CRUD operations for summary

# Get summary of expenses
def get_summary():

    response = requests.get(
        f"{BASE_URL}/summary"
    )

    return response

# Get summary of expenses by category
def get_category_summary():

    response = requests.get(
        f"{BASE_URL}/summary/category"
    )

    return response

# Get summary of expenses by month
def get_monthly_summary():

    response = requests.get(
        f"{BASE_URL}/summary/monthly"
    )

    return response

# Get all unique expense categories for filtering in the home page, if not provided, it will return all categories
def get_categories():

    response = requests.get(
        f"{BASE_URL}/expenses/categories"
    )

    return response