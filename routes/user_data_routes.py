from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import db_connection

from logic.register_and_login import (
    register_new_user,
)
from models.schemas.create_user_schema import UserCreate

auth_router = APIRouter()

def get_db():
    db = db_connection()
    try:
        yield db
    finally:
        db.close()

@auth_router.post("/user/register")
async def create_user(user_data: UserCreate, session: Session = Depends(get_db)):
    """
    Create a new user.

    Args:
        user_data (UserCreate): User data to create the user.
        session (Session): Database session.

    Returns:
        dict: Message indicating successful user creation.
    """
    try:
        await register_new_user(user_data, session)
        return {"message": "User created successfully"}
    except HTTPException as e:
        raise e
