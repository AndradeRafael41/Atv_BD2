
from typing import Optional
from sqlalchemy import Integer, PrimaryKeyConstraint, String
from sqlalchemy.orm import  Mapped, mapped_column
from .base import Base

class Categories(Base):
    __tablename__ = 'categories'
    __table_args__ = (
        PrimaryKeyConstraint('categoryid', name='categories_pkey'),
        {'schema': 'northwind'}
    )

    categoryid: Mapped[int] = mapped_column(Integer, primary_key=True)
    categoryname: Mapped[Optional[str]] = mapped_column(String(50))
    description: Mapped[Optional[str]] = mapped_column(String(100))