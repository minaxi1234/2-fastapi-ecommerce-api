from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from database.models.cart import Cart, CartItem
from database.models.product import Product
from database.models.user import User
from schemas.cart import CartItemCreate

class CartService:
    def __init__(self, db: Session):
        self.db = db

    # FIXED: This method now returns Cart object for internal use
    def get_or_create_cart(self, user_email: str) -> Cart:
        user = self.db.query(User).filter(User.email == user_email).first()
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        cart = self.db.query(Cart).filter(Cart.user_id == user.id).first()

        if not cart:
            cart = Cart(user_id=user.id)
            self.db.add(cart)
            self.db.commit()
            self.db.refresh(cart)
        
        # RETURN the Cart model object directly, NOT make_cart_response
        return cart
  
    def add_item_to_cart(self, user_email: str, item_data: CartItemCreate) -> dict:
        # get_or_create_cart returns Cart object, not dict
        cart_obj = self.get_or_create_cart(user_email)

        product = self.db.query(Product).filter(Product.id == item_data.product_id).first()
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            )
        
        # Now cart_obj is a Cart model with .id attribute
        existing_item = self.db.query(CartItem).filter(
            CartItem.product_id == item_data.product_id, 
            CartItem.cart_id == cart_obj.id  
        ).first()
        
        if existing_item:
            existing_item.quantity += item_data.quantity
        else:
            new_item = CartItem(
                cart_id=cart_obj.id,  # This now works
                product_id=item_data.product_id,
                quantity=item_data.quantity
            )
            self.db.add(new_item)
        
        self.db.commit()
        
        # Convert to response format ONLY at the end
        return self.make_cart_response(cart_obj)

    def make_cart_response(self, cart: Cart) -> dict:
        """Convert database cart to API response"""
        total_amount = 0
        total_items = 0
        items_list = []
        
        for item in cart.items:
            product = self.db.query(Product).filter(Product.id == item.product_id).first()
            
            items_list.append({
                "id": item.id,
                "cart_id": item.cart_id,
                "product_id": item.product_id,
                "product_name": product.name,
                "quantity": item.quantity,
                "unit_price": product.price,
                "total_price": product.price * item.quantity,
                "created_at": item.created_at
            })
            
            total_amount += product.price * item.quantity
            total_items += item.quantity
        
        return {
            "id": cart.id,
            "user_id": cart.user_id,
            "items": items_list,
            "total_amount": total_amount,
            "total_items": total_items,
            "created_at": cart.created_at,
            "updated_at": cart.updated_at
        }
    


    def remove_item_from_cart(self, user_email: str, item_id: int) -> dict:
  
        cart = self.get_or_create_cart(user_email)

        item = self.db.query(CartItem).filter(
            CartItem.id == item_id,
            CartItem.cart_id == cart.id
        ).first()

        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Item not found in cart"
            )

        self.db.delete(item)
        self.db.commit()

        return self.make_cart_response(cart)