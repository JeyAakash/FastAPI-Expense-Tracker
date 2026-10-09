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
