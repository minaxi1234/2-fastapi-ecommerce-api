from sqlalchemy import String, Column, Integer, Text, ForeignKey
from database.config import Base
from sqlalchemy.orm import relationship

class Category(Base):
  __tablename__ = "categories"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(100), unique=True, nullable=False)
  description = Column(Text)
  slug = Column(String(100), unique=True, nullable=False)

  # relationship

  products = relationship("Product", back_populates="category")





  