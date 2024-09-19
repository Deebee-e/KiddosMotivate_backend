from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    username: str = Field(..., min_length=7, description="Invalid username")
    email: EmailStr = Field(..., description="Invalid email address")
    password: str = Field(..., min_length=7, description="Password must be greater than 6 characters")

    class Config:
        json_schema_extra = {
            "example": {
                "username": "sample_username",
                "email": "sample@example.com",
                "password": "sample_password",
            }
        }
