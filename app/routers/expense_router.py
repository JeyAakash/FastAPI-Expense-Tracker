from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas, auth
from app.database import get_db

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post("", response_model=schemas.ExpenseResponse, status_code=status.HTTP_201_CREATED)
def create_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    db_expense = models.Expense(**expense.model_dump(), user_id=current_user.id)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

@router.get("", response_model=List[schemas.ExpenseResponse])
def read_expenses(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    return db.query(models.Expense).filter(
        models.Expense.user_id == current_user.id
    ).offset(skip).limit(limit).all()

@router.get("/{id}", response_model=schemas.ExpenseResponse)
def read_expense(
    id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    expense = db.query(models.Expense).filter(
        models.Expense.id == id,
        models.Expense.user_id == current_user.id
    ).first()
    
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found")
    return expense

@router.put("/{id}", response_model=schemas.ExpenseResponse)
def update_expense(
    id: int,
    expense_data: schemas.ExpenseUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    expense_query = db.query(models.Expense).filter(
        models.Expense.id == id,
        models.Expense.user_id == current_user.id
    )
    expense = expense_query.first()

    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found")

    update_data = expense_data.model_dump(exclude_unset=True)
    expense_query.update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(expense)
    return expense

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expense(
    id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    expense = db.query(models.Expense).filter(
        models.Expense.id == id,
        models.Expense.user_id == current_user.id
    ).first()

    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found")

    db.delete(expense)
    db.commit()
    return None