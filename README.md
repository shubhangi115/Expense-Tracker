# Expense Tracker

A simple Expense Tracker application built with **FastAPI**, **Streamlit**, and **SQLite**.

## Features

- Add, update, and delete expenses
- View all expenses
- Filter expenses by category
- SQLite database for storage

## Tech Stack

- Python
- FastAPI
- Streamlit
- SQLite

## Setup

### Clone the repository

```bash
git clone https://github.com/shubhangi115/Expense-Tracker.git
cd Expense-Tracker
```

### Create and activate a virtual environment

**Windows**

```bash
python -m venv expense_venv
expense_venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv expense_venv
source expense_venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Run the application

Start the FastAPI backend:

```bash
uvicorn app.main:app --reload
```

In a new terminal, start the Streamlit frontend:

```bash
streamlit run frontend/main.py
```

## API Documentation

Once the backend is running:

```
http://127.0.0.1:8000/docs
```

---

