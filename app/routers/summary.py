from fastapi import APIRouter

from app import crud

router = APIRouter(prefix="/summary", tags=["Analytics"])


@router.get("")
def get_summary():
    """Get a summary of expenses from the database."""
    expense_summary = crud.get_summary()
    return expense_summary


@router.get("/category")
def category_summary():
    """Get a summary of expenses by category from the database."""
    category_expense_summary = crud.category_summary()
    return category_expense_summary


@router.get("/monthly")
def monthly_summary():
    """Get a summary of expenses by month from the database."""
    monthly_expense_summary = crud.monthly_summary()
    return monthly_expense_summary