from fastapi import FastAPI

# for the databse to be used
from app.database import initialize_database

# for the endpoints
from app.routers import health, expenses, summary

from app.routers import (
    health,
    expenses,
    summary,
)

# Create the FastAPI application
app = FastAPI(
    title="Expense Tracker API",
    description="Backend API for the Expense Tracker project."
)

initialize_database()

app.include_router(health.router)
app.include_router(expenses.router)
app.include_router(summary.router)


@app.get("/")
def root():
    """
    check endpoint to verify that the API server is running.
    """
    return {
        "message": "Expense Tracker API is running successfully!"
    }