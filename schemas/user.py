from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
  email: EmailStr
  first_name: str = Field(min_length=1, max_length=100)
  last_name: str = Field(min_length=1, max_length=100)

class UserCreate(UserBase):
  password: str = Field(min_length=8, max_length=100)

class UserResponse(UserBase):
  id: int
  is_active: bool
  is_superuser: bool
  created_at: datetime

  class Config:
    from_attributes = True

class UserLogin(BaseModel):
  email: EmailStr
  password: str

class Token(BaseModel):
  access_token: str
  token_type: str







