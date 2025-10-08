from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime



class CartItemBase(BaseModel):
  product_id: int
  quantity: int = Field(ge=1 , le=100)

class CartItemCreate(CartItemBase):
  pass

class CartItemResponse(CartItemBase):
  id: int
  cart_id: int
  product_name: str
  unit_price: float
  total_price: float
  created_at: datetime

  class Config:
    from_attributes = True

class CartBase(BaseModel):
  pass
class CartResponse(CartBase):
  id: int
  user_id: int
  items: List[CartItemResponse] = []
  total_amount:float
  total_items: int
  created_at: datetime
  updated_at: Optional[datetime] = None
    
  class Config:
    from_attributes = True

