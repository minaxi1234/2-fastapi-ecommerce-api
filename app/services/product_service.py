from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from database.models.product import Product
from database.models.category import Category
from schemas.product import ProductCreate, ProductResponse


class ProductService:
  def __init__(self, db:Session):
    self.db = db

  def create_product(self, product_data: ProductCreate) -> Product:
    category = self.db.query(Category).filter(Category.id == product_data.category_id).first()
    if not category:
      raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Category not found"
      )
    existing_product = self.db.query(Product).filter(Product.sku == product_data.sku).first()
    if existing_product:
      raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Product with this SKU already exists"
      )
    new_product = Product(
            name=product_data.name,
            description=product_data.description,
            price=product_data.price,
            stock_quantity=product_data.stock_quantity,
            sku=product_data.sku,
            is_active=product_data.is_active,
            is_featured=product_data.is_featured,
            category_id=product_data.category_id
        )
        
    self.db.add(new_product)
    self.db.commit()
    self.db.refresh(new_product)
    
    return new_product

  def get_all_products(self) -> list[Product]:
    return self.db.query(Product).filter(Product.is_active == True).all()
  
  def get_product_by_id(self, product_id: int) ->Product:
    product = self.db.query(Product).filter(Product.id == product_id).first()
    if not product:
      raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            ) 
    return product





  def update_product(self, product_id: int, product_data: ProductCreate) -> Product:
      product = self.get_product_by_id(product_id)
      
  
      if product_data.sku != product.sku:
          existing_sku = self.db.query(Product).filter(
              Product.sku == product_data.sku,
              Product.id != product_id
          ).first()
          if existing_sku:
              raise HTTPException(
                  status_code=status.HTTP_400_BAD_REQUEST,
                  detail="Product with this SKU already exists"
              )
      

      category = self.db.query(Category).filter(Category.id == product_data.category_id).first()
      if not category:
          raise HTTPException(
              status_code=status.HTTP_404_NOT_FOUND,
              detail="Category not found"
          )

      product.name = product_data.name
      product.description = product_data.description
      product.price = product_data.price
      product.stock_quantity = product_data.stock_quantity
      product.sku = product_data.sku
      product.is_active = product_data.is_active
      product.is_featured = product_data.is_featured
      product.category_id = product_data.category_id
      
      self.db.commit()
      self.db.refresh(product)
      
      return product

  def  delete_product(self, product_id: int) -> None:
     product = self.get_product_by_id(product_id)

     self.db.delete(product)
     self.db.commit()

  def get_products_by_category(self, category_id: int) -> list[Product]:
     category = self.db.query(Category).filter(Category.id == category_id).first()
     if not category:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found"
            )
     return self.db.query(Product).filter(Product.category_id == category_id, Product.is_active == True).all()
  
    






















    




