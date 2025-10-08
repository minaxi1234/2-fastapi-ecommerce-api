from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.config import get_db
from database.services.jwt import get_current_user
from database.models.user import User
from schemas.order import OrderCreate, OrderResponse
from app.services.order_services import OrderService



router = APIRouter(
  prefix = "/api/v1/orders",
  tags = ["orders"]
)


@router.post("/checkout", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(
  order_data: OrderCreate,
  current_user: User = Depends(get_current_user),
  db: Session = Depends(get_db)
):
  print(f"🔍 DEBUG: current_user type: {type(current_user)}, value: {current_user}")
  try:
    order = OrderService.create_order_from_cart(
      db= db,
      user_id = current_user.id,
      shipping_address=order_data.shipping_address
    )
    return order
  except ValueError as e:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail=str(e)
    )
  except Exception as e:
    print(f"Unexpected error: {str(e)}")
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Failed to create order"
        )

