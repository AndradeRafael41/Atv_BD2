
from typing import Optional
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
import decimal
from .base import Base

if TYPE_CHECKING:
    from .orders import Orders
    from .products import Products


class OrderDetails(Base):
    __tablename__ = 'order_details'
    __table_args__ = (
        ForeignKeyConstraint(['orderid'], ['northwind.orders.orderid'], name='order_relation'),
        ForeignKeyConstraint(['productid'], ['northwind.products.productid'], name='product_relation'),
        PrimaryKeyConstraint('orderid', 'productid', name='order_details_pkey'),
        {'schema': 'northwind'}
    )

    orderid: Mapped[int] = mapped_column(Integer, primary_key=True)
    productid: Mapped[int] = mapped_column(Integer, primary_key=True)
    unitprice: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(13, 4))
    quantity: Mapped[Optional[int]] = mapped_column(SmallInteger)
    discount: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 4))

    orders: Mapped['Orders'] = relationship('Orders', back_populates='order_details')
    products: Mapped['Products'] = relationship('Products', back_populates='order_details')