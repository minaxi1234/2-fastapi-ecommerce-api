from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from database.models.user import User
from schemas.user import UserCreate, UserResponse
from database.services.password import hash_password, verify_password

class UserService():
  def __init__(self, db: Session):
    self.db = db


  def create_user(self, user_data: UserCreate) -> User:
    existing_user = self.db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
      raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="User with this email already exists"
      )
    new_user = User(
      email= user_data.email,
      first_name= user_data.first_name,
      last_name= user_data.last_name,
      password= hash_password(user_data.password)
    )

    self.db.add(new_user)
    self.db.commit()
    self.db.refresh(new_user)
    return new_user
  

  def get_user_by_email(self, email: str) -> User:

    user = self.db.query(User).filter(User.email == email).first()

    if not user:
      raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
      )
    return user
  
  def authenticate_user(self,email:str, password:str)-> User:
    user = self.db.query(User).filter(User.email == email).first()
    if not user:
      raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
          )
    
    if not verify_password(password, user.password):
      raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
          )
    
    return user










    