from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database.config import Base

class Address(Base):
  __tablename__ = 'addresses'

  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

  street = Column(String(255), nullable=False)
  city = Column(String(100), nullable=False)
  state = Column(String(255), nullable=False)
  country = Column(String(255), nullable=False)
  postal_code = Column(String(20), nullable=False)
  is_primary = Column(Boolean, default=False)

  user = relationship("User", back_populates="addresses")