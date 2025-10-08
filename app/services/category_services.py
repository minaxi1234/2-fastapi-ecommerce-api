from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from database.models.category import Category
from schemas.product import CategoryCreate

class CategoryService:
    def __init__(self, db: Session):
        self.db = db

    def create_category(self, category_data: CategoryCreate):
        # Check if category name already exists
        existing_category = self.db.query(Category).filter(
            Category.name == category_data.name
        ).first()
        
        if existing_category:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Category with this name already exists"
            )
        
        new_category = Category(
            name=category_data.name,
            description=category_data.description,
            slug=category_data.slug
        )
        
        self.db.add(new_category)
        self.db.commit()
        self.db.refresh(new_category)
        return new_category