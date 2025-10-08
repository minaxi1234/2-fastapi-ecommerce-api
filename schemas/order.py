from pydantic import BaseModel
from datetime import datetime
from typing import List
from enum import Enum

class OrderStatus(str, Enum):
  PENDING = "pending"  
  CONFIRMED = "confirmed"  
  SHIPPED = "shipped"    
  DELIVERED = "delivered" 
  CANCELLED = "cancelled"

class OrderItemBase(BaseModel):
  product_id: int
  quantity: int
  unit_price: float

class OrderItemCreate(OrderItemBase):
    pass

class OrderCreate(BaseModel):
  shipping_address: str

class OrderResponse(OrderCreate):
  id: int
  order_number: str
  total_amount: float
  status: OrderStatus
  created_at: datetime
  user_id: int

  class Config:
    from_attributes = True
