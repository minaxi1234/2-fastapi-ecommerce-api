from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database.config import Base
import enum

class OrderStatus(enum.Enum):
  PENDING = "pending"
  CONFIRMED = "confirmed"
  PROCESSING = "processing"
  SHIPPED = "shipped"
  DELIVERED = "delivered"
  CANCELLED = "cancelled"

class Order(Base):
  __tablename__ = "orders"

  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
  order_number = Column(String(50), unique=True, nullable=False)
  total_amount = Column(Float, nullable=False)
  status = Column(Enum(OrderStatus), default=OrderStatus.PENDING)

  shipping_address = Column(String(500), nullable=False)

  created_at = Column(DateTime(timezone=True), server_default=func.now())
  updated_at = Column(DateTime(timezone=True), onupdate=func.now())

  user = relationship("User", back_populates="orders")

  order_items = relationship("OrderItem", back_populates="order")







