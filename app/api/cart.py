from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database.config import get_db
from app.services.cart_services import CartService
from schemas.cart import CartResponse, CartItemCreate
from database.services.jwt import get_current_user


router = APIRouter()

@router.post("/add-item", response_model=CartResponse)
def add_item_to_cart(
  item_data: CartItemCreate,
  db: Session = Depends(get_db),
  current_user: dict = Depends(get_current_user)
):
  cart_service = CartService(db)
  cart = cart_service.add_item_to_cart(current_user.email, item_data)
  return cart

@router.get("/", response_model=CartResponse)
def get_cart(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    cart_service = CartService(db)
    cart = cart_service.get_or_create_cart(current_user.email)
    return cart_service.make_cart_response(cart)

@router.delete("/{item_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_items_from_cart(
  item_id:int,
  current_user: dict = Depends(get_current_user),
  db: Session = Depends(get_db)
):
  cart_service = CartService(db)
  cart = cart_service.remove_item_from_cart(current_user.email, item_id)
  return None



