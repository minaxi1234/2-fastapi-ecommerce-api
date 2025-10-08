from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class CategoryBase(BaseModel):
  name: str = Field(..., min_length=1, max_length=100)
  description: Optional[str] = None
  slug: str = Field(..., min_length=1, max_length=100)

class CategoryCreate(CategoryBase):
  pass

class CategoryResponse(CategoryBase):
  id: int
  class Config:
    from_attributes = True

class ProductImageBase(BaseModel):
  image_url: set
  alt_text: Optional[str] = None
  is_primary: bool = False

class ProductImageCreate(ProductImageBase):
  pass

class ProductImageResponse(ProductImageBase):
  id: int
  product_id: int
  class Config:
    from_attributes = True

class ProductBase(BaseModel):
  name: str = Field(..., min_length=1, max_length=255)
  description:  Optional[str] = None
  price: float = Field(..., gt=0)
  stock_quantity: int = Field(..., ge=0)
  sku: str = Field(..., min_length=1, max_length=100)
  is_active: bool= True
  is_featured: bool = False
  category_id: int

class ProductCreate(ProductBase):
  pass

class ProductResponse(ProductBase):
  id: int
  created_at: datetime
  updated_at: Optional[datetime] = None
  class Config:
    from_attributes= True


  