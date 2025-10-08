from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime
import random
import string

from database.models.order import Order, OrderStatus
from database.models.order_item import OrderItem
from database.models.cart import Cart,CartItem


def generate_order_number() -> str:
  timestamp = datetime.now().strftime("%Y%m%d")

  random_char = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

  return f"ORD-{timestamp}-{random_char}"

class OrderService:

  @staticmethod
  def create_order_from_cart(db: Session, user_id: int, shipping_address: str) -> Order:
    cart_stmt = select(Cart).where(Cart.user_id == user_id)
    cart = db.execute(cart_stmt).scalar_one_or_none()
    print(f"🔍 DEBUG 1: Cart type: {type(cart)}")
    if not cart:
      raise ValueError("Shopping cart not found")
    if not cart.items:
      raise ValueError("Cannot checkout empty cart")
    
    total_amount = 0.0

    for cart_item in cart.items:
      item_total = cart_item.product.price * cart_item.quantity
      total_amount += item_total

    order = Order(
      user_id = user_id,
      order_number = generate_order_number(),
      total_amount = total_amount,
      status = OrderStatus.PENDING,
      shipping_address = shipping_address
    )
    print(f"🔍 DEBUG 2: Order type: {type(order)}")  # ADD THIS
    print(f"🔍 DEBUG 3: Order attributes: {dir(order)}") 
    db.add(order)
    db.flush()

    for cart_item in cart.items:
      order_item = OrderItem(
        order_id = order.id,
        product_id= cart_item.product_id,
        quantity = cart_item.quantity,
        unit_price = cart_item.product.price
      )
      db.add(order_item)

    for cart_item in cart.items:
        db.delete(cart_item)
    db.commit()
    db.refresh(order)  
    
    return order








