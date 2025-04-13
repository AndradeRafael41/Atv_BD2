from typing import List, Optional
from sqlalchemy import  Integer, Numeric, PrimaryKeyConstraint, SmallInteger, String
from sqlalchemy.orm import  Mapped, mapped_column, relationship
import decimal
from .base import Base
from .orderDetails import OrderDetails


class Products(Base):
    __tablename__ = 'products'
    __table_args__ = (
        PrimaryKeyConstraint('productid', name='products_pkey'),
        {'schema': 'northwind'}
    )

    productid: Mapped[int] = mapped_column(Integer, primary_key=True)
    supplierid: Mapped[int] = mapped_column(Integer)
    categoryid: Mapped[int] = mapped_column(Integer)
    productname: Mapped[Optional[str]] = mapped_column(String(35))
    quantityperunit: Mapped[Optional[str]] = mapped_column(String(20))
    unitprice: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(13, 4))
    unitsinstock: Mapped[Optional[int]] = mapped_column(SmallInteger)
    unitsonorder: Mapped[Optional[int]] = mapped_column(SmallInteger)
    reorderlevel: Mapped[Optional[int]] = mapped_column(SmallInteger)
    discontinued: Mapped[Optional[str]] = mapped_column(String(1))

    order_details: Mapped[List['OrderDetails']] = relationship('OrderDetails', back_populates='products')