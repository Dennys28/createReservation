from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import datetime


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, nullable=False)
    table_id = Column(Integer, nullable=False)
    restaurant_id = Column(Integer, nullable=False)
    reservation_time = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, default="Pending")
