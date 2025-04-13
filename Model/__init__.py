
# transformando a pasta model em um módulo python (facilita o uso e importação)
from .base import Base
from .categories import Categories
from .costumers import Customers
from .employees import Employees
from .orderDetails import OrderDetails
from .orders import Orders
from .products import Products
from .shippers import Shippers
from .suppliers import Suppliers

__all__ = ["Base", "Categories", "Customers","Employees","OrderDetails","Orders","Products","Shippers","Suppliers"]