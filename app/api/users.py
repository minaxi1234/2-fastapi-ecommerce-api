from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database.config import get_db
from schemas.user import UserCreate, UserResponse,UserLogin,Token
from app.services.user_service import UserService
from database.services.jwt import create_access_token, get_current_user

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user_data:UserCreate, db: Session= Depends(get_db)):
  user_service = UserService(db)

  user = user_service.create_user(user_data)
  return user

@router.post("/login", response_model=Token)
def login_user(login_data: UserLogin, db: Session= Depends(get_db)):
  user_service = UserService(db)

  user = user_service.authenticate_user(login_data.email, login_data.password)

  access_token = create_access_token(data={"sub":user.email})
  return {"access_token": access_token, "token_type": "bearer"}

@router.post("/me", response_model = UserResponse)
def get_current_user(current_user:dict = Depends(get_current_user), db: Session= Depends(get_db)):
  user_service = UserService(db)
  user = user_service.get_user_by_email(current_user["sub"])

  return user











