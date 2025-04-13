from typing import List, Optional
from typing import TYPE_CHECKING
from sqlalchemy import DateTime, Integer,  PrimaryKeyConstraint, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime
from .base import Base


if TYPE_CHECKING:
    from .orders import Orders
    
class Employees(Base):
    __tablename__ = 'employees'
    __table_args__ = (
        PrimaryKeyConstraint('employeeid', name='employees_pkey'),
        {'schema': 'northwind'}
    )

    employeeid: Mapped[int] = mapped_column(Integer, primary_key=True)
    lastname: Mapped[Optional[str]] = mapped_column(String(10))
    firstname: Mapped[Optional[str]] = mapped_column(String(10))
    title: Mapped[Optional[str]] = mapped_column(String(25))
    titleofcourtesy: Mapped[Optional[str]] = mapped_column(String(5))
    birthdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    hiredate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    address: Mapped[Optional[str]] = mapped_column(String(50))
    city: Mapped[Optional[str]] = mapped_column(String(20))
    region: Mapped[Optional[str]] = mapped_column(String(2))
    postalcode: Mapped[Optional[str]] = mapped_column(String(9))
    country: Mapped[Optional[str]] = mapped_column(String(15))
    homephone: Mapped[Optional[str]] = mapped_column(String(14))
    extension: Mapped[Optional[str]] = mapped_column(String(4))
    reportsto: Mapped[Optional[int]] = mapped_column(Integer)
    notes: Mapped[Optional[str]] = mapped_column(Text)

    orders: Mapped[List['Orders']] = relationship('Orders', back_populates='employees')