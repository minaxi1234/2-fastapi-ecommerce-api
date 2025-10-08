from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database.config import Base

class Cart(Base):
  __tablename__ = "carts"
  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
  created_at = Column(DateTime(timezone=True), server_default=func.now())
  updated_at = Column(DateTime(timezone=True), onupdate=func.now())

  user = relationship("User", back_populates="cart")
  items = relationship("CartItem", back_populates="cart")

class CartItem(Base):
  __tablename__ = "cart_items"

  id = Column(Integer, primary_key=True, index=True)
  cart_id = Column(Integer, ForeignKey("carts.id"), nullable=False)
  product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
  quantity = Column(Integer, default=1, nullable=False)
  created_at = Column(DateTime(timezone=True), server_default=func.now())
  cart = relationship("Cart", back_populates="items")
  product = relationship("Product",back_populates="cart_items")

