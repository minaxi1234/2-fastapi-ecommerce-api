from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database.config import get_db
from schemas.product import ProductCreate, ProductResponse
from app.services.product_service import ProductService

router = APIRouter()

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product_data: ProductCreate, db: Session = Depends(get_db)):
  product_services = ProductService(db)
  product = product_services.create_product(product_data)
  return product

@router.get("/", response_model=list[ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
  product_services = ProductService(db)
  products = product_services.get_all_products()
  return products

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
  product_services = ProductService(db)
  product = product_services.get_product_by_id(product_id)
  return product

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product_data:ProductCreate, db: Session = Depends(get_db)):
  product_service = ProductService(db)
  product = product_service.update_product(product_id, product_data)
  return product

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id:int, db : Session = Depends(get_db)):
  product_services = ProductService(db)
  product_services.delete_product(product_id)
  return None


@router.get("/category/{category_id}", response_model=list[ProductResponse])
def get_products_by_category(category_id: int, db: Session = Depends(get_db)):
  product_services = ProductService(db)
  products = product_services.get_products_by_category(category_id)
  return products













