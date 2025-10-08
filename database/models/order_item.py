from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database.config import Base


class OrderItem(Base):
  __tablename__ = "order_items"
  id = Column(Integer, primary_key=True, index=True)
  order_id = Column(Integer, ForeignKey("orders.id"))
  product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

  quantity = Column(Integer, nullable=False, default=1)
  unit_price = Column(Float,  nullable=False)

  order = relationship("Order", back_populates="order_items")
  product = relationship("Product", back_populates="order_items")



