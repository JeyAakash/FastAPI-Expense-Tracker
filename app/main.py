from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth_router, expense_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Expense Tracker REST API",
    description="A FastAPI backend featuring JWT Auth and strict User-Owned CRUD resources.",
    version="1.0.0"
)

app.include_router(auth_router.router)
app.include_router(expense_router.router)

@app.get("/")
def root():
    return {"message": "Welcome to Expense Tracker API. Visit /docs for Swagger UI documentation."}