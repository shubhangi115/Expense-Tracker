from fastapi import APIRouter, Query

from app.schemas import ExpenseCreate
from app import crud
from fastapi import HTTPException

router = APIRouter(prefix="/expenses", tags=["Expenses"])


@router.post("", status_code=201)
def create_expense(expense: ExpenseCreate):
    """Creating a new expense"""

    crud.create_expense(expense)

    return {
        "message": "Expense created successfully."
    }


@router.get("")
def get_expenses(
    expense_type: str | None = Query(default=None),
    category: str | None = Query(default=None)
):  # ---> so that we can filter the expenses by type and category for filter in the home page, if not provided, it will return all expenses
    """
    Get all expenses from database
    """

    expenses = crud.get_expenses(expense_type,
    category
)

    return expenses

# added new endpoint to get all unique expense categories for the filter in the home page
@router.get("/categories")
def get_categories():
    """Get all unique expense categories."""

    return crud.get_categories()


@router.get("/{expense_id}")
def get_expense(expense_id: int):
    """
    Get a single expense by its ID.
    """

    expense = crud.get_expense(expense_id)

    if not expense :
        raise HTTPException(status_code=404, detail=f"Expense with ID {expense_id} not found.")

    return expense


@router.put("/{expense_id}")
def update_expense(expense_id: int, user_sent_expense: ExpenseCreate):
    """
    Update an existing expense by its ID.
    """
    exisitng_expense = crud.get_expense(expense_id)

    if not exisitng_expense :
        raise HTTPException(status_code=404, detail=f"Expense with ID {expense_id} not found.")

    # return crud.update_expense(expense_id, user_sent_expense)
    crud.update_expense(expense_id, user_sent_expense)

    return {
    "message": "Expense updated successfully."
}



@router.delete("/{expense_id}")
def delete_expense(expense_id: int):
    """
    Delete an existing expense by its ID.
    """

    expense = crud.get_expense(expense_id)

    if not expense :
        raise HTTPException(status_code=404, detail=f"Expense with ID {expense_id} not found.")

    crud.delete_expense(expense_id)

    return {
        "message": "Expense deleted successfully."
    }


