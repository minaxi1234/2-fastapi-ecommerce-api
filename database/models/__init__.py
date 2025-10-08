# Make models a proper Python package
from .user import User
from .address import Address
from .category import Category
from .product import Product
from .product_image import ProductImage
from .order import Order
from .order_item import OrderItem

__all__ = [
    "User",
    "Address", 
    "Category",
    "Product",
    "ProductImage",
    "Order",
    "OrderItem"
]