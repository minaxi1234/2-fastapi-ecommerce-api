from sqlalchemy import Column, Integer, String, Text, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database.config import Base

class Product(Base):
  __tablename__ = "products"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(255), nullable=False)
  description = Column(Text)
  stock_quantity = Column(Integer, default=0)
  sku = Column(String(100), unique=True, nullable=False)
  is_active = Column(Boolean, default=True)
  is_featured = Column(Boolean, default=False)
  price = Column(Float, nullable=False)

  created_at = Column(DateTime(timezone=True), server_default=func.now())
  updated_at = Column(DateTime(timezone=True), onupdate=func.now())

  category_id = Column(Integer, ForeignKey("categories.id"))
  # relqtionsh
  category = relationship("Category", back_populates="products")
  images = relationship("ProductImage", back_populates="product")
  order_items = relationship("OrderItem", back_populates="product")
  cart_items = relationship("CartItem", back_populates="product")





 