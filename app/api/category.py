from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database.config import get_db
from schemas.product import CategoryCreate, CategoryResponse
from app.services.category_services import CategoryService

router = APIRouter()

@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category_data: CategoryCreate, db: Session = Depends(get_db)):
    category_service = CategoryService(db)
    category = category_service.create_category(category_data)
    return category