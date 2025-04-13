from typing import List, Optional
from typing import TYPE_CHECKING
from sqlalchemy import DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String
from sqlalchemy.orm import  Mapped, mapped_column, relationship
import datetime
import decimal
from .base import Base

if TYPE_CHECKING:
    from .costumers import Customers
    from .employees import Employees
    from .orderDetails import OrderDetails

class Orders(Base):
    __tablename__ = 'orders'
    __table_args__ = (
        ForeignKeyConstraint(['customerid'], ['northwind.customers.customerid'], name='customers_relation'),
        ForeignKeyConstraint(['employeeid'], ['northwind.employees.employeeid'], name='employess_relation'),
        PrimaryKeyConstraint('orderid', name='orders_pkey'),
        {'schema': 'northwind'}
    )

    orderid: Mapped[int] = mapped_column(Integer, primary_key=True)
    customerid: Mapped[str] = mapped_column(String(5))
    employeeid: Mapped[int] = mapped_column(Integer)
    orderdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    requireddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    shippeddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    freight: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(15, 4))
    shipname: Mapped[Optional[str]] = mapped_column(String(35))
    shipaddress: Mapped[Optional[str]] = mapped_column(String(50))
    shipcity: Mapped[Optional[str]] = mapped_column(String(15))
    shipregion: Mapped[Optional[str]] = mapped_column(String(15))
    shippostalcode: Mapped[Optional[str]] = mapped_column(String(9))
    shipcountry: Mapped[Optional[str]] = mapped_column(String(15))
    shipperid: Mapped[Optional[int]] = mapped_column(Integer)

    customers: Mapped['Customers'] = relationship('Customers', back_populates='orders')
    employees: Mapped['Employees'] = relationship('Employees', back_populates='orders')
    order_details: Mapped[List['OrderDetails']] = relationship('OrderDetails', back_populates='orders')