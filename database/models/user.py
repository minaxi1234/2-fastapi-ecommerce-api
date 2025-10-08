from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import  func
from database.config import Base
from sqlalchemy.orm import relationship


class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, index=True)
  email = Column(String(255), unique=True, nullable=False, index=True)
  password= Column(String(255), nullable=False)
  first_name = Column(String(255), nullable=False)
  last_name = Column(String(100), nullable=False)
  is_active = Column(Boolean, default=True)
  is_superuser = Column(Boolean, default=False)
  created_at = Column(DateTime(timezone=True), server_default=func.now())
  updated_at = Column(DateTime(timezone=True), onupdate=func.now())

  # relationships

  addresses = relationship("Address", back_populates="user")
  orders = relationship("Order", back_populates="user")
  cart = relationship("Cart", back_populates="user", uselist=False)

