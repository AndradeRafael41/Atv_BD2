from typing import  Optional
from sqlalchemy import Integer, PrimaryKeyConstraint, SmallInteger, String, Text
from sqlalchemy.orm import  Mapped, mapped_column
from .base import Base


class Shippers(Base):
    __tablename__ = 'shippers'
    __table_args__ = (
        PrimaryKeyConstraint('shipperid', name='shippers_pkey'),
        {'schema': 'northwind'}
    )

    shipperid: Mapped[int] = mapped_column(Integer, primary_key=True)
    companyname: Mapped[Optional[str]] = mapped_column(String(20))
    phone: Mapped[Optional[str]] = mapped_column(String(14))