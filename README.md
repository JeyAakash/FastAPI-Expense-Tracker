# Expense Tracker
A lightweight, secure RESTful API built with **FastAPI**, **SQLAlchemy**, and **Pydantic v2**. This application provides user authentication using JWT and argon2/bcrypt password hashing, alongside full CRUD operations for managing personal expenses.

---

## Features

- **User Authentication:** Registration, login, JWT token generation (`OAuth2PasswordBearer`), and secure password hashing via `pwdlib[argon2]`.
- **Expense CRUD Operations:** Create, read (list & single item), update, and delete expenses tied specifically to the authenticated user.
- **Data Validation:** Strict input/output validation powered by Pydantic v2.
- **Interactive Documentation:** Auto-generated Swagger UI (`/docs`) and ReDoc (`/redoc`).
- **Database:** SQLite local storage managed via SQLAlchemy ORM.

---

## Tech Stack

- **Framework:** FastAPI
- **Language:** Python 3.13
- **ORM:** SQLAlchemy (SQLite)
- **Validation:** Pydantic v2
- **Authentication:** `pwdlib[argon2]`, `python-jose`, `OAuth2PasswordBearer`
- **Server:** Uvicorn

---

## Project Structure

```text
fastapi-expense-tracker/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application & route inclusion
│   ├── auth.py          # JWT utilities & password hashing
│   ├── config.py        # Environment settings (Pydantic Settings)
│   ├── database.py      # SQLAlchemy engine & session setup
│   ├── models.py        # SQLAlchemy database models (User, Expense)
│   ├── schemas.py       # Pydantic schemas for request/response validation
│   └── routers/
│       ├── auth.py      # Authentication routes (/auth/register, /auth/login)
│       └── expenses.py  # Expense CRUD routes (/expenses)
├── .env.example         # Template for environment variables
├── .gitignore           # Git ignore rules (.venv, app.db, .env)
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies

Installation & Setup
1. Clone the Repository
git clone https://github.com/JeyAakash/FastAPI-Expense-Tracker.git 
cd fastapi-expense-tracker

2. Set Up Virtual Environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables
Copy the .env.example file to create your local .env configuration:
Copy-Item .env.example .env

Running the Application
Start the Uvicorn development server:

uvicorn app.main:app --reload
Interactive API Docs (Swagger UI): http://127.0.0.1:8000/docs

MethodEndpointDescriptionAuth RequiredPOST/auth/registerRegister a new user accountNoPOST/auth/loginAuthenticate and retrieve JWT access tokenNoGET/expensesRetrieve all expenses for current userYesPOST/expensesCreate a new expense entryYesGET/expenses/{id}Retrieve details of a specific expenseYesPUT/expenses/{id}Update an existing expense recordYesDELETE/expenses/{id}Remove an expense recordYes
