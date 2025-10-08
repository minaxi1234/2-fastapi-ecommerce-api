import os
from datetime import datetime, timedelta
from jose import JWTError, jwt
from dotenv import load_dotenv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import HTTPException,status, Depends
from database.models.user import User
from sqlalchemy.orm import Session
from database.config import get_db
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "your_fallback_secret_key_change_in_production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data:dict, expires_delta: timedelta = None):
  to_encode = data.copy()
  if expires_delta:
    expires = datetime.utcnow() + expires_delta
  else:
    expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp": expires})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY,algorithm=ALGORITHM)
  return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
    
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials=Depends(security),db: Session = Depends(get_db)):
   token = credentials.credentials
   payload = verify_token(token)

   if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
   email = payload.get("sub")
   if email is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    
    # Get user from database
   user = db.query(User).filter(User.email == email).first()
   if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    
   return user
 





