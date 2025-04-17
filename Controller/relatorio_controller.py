from DB.DaoOrm import GenericDAO, SessionLocal
from Model.orders import Orders
from Model.costumers import Customers
from Model.employees import Employees
from Model.shippers import Shippers
from Model.products import Products
from Model.orderDetails import OrderDetails
from sqlalchemy import func, distinct
from sqlalchemy.orm import joinedload

import datetime

from tabulate import tabulate


class RelatorioController:
    
    def __init__(self):
        self.session = SessionLocal()
        self.dao = GenericDAO(self.session, Orders)
        self.cliente_dao = GenericDAO(self.session, Customers)
        self.funcionario_dao = GenericDAO(self.session, Employees)
        self.entregador_dao = GenericDAO(self.session, Shippers)
        self.produto_dao = GenericDAO(self.session, Products)
        
    def listar_pedidos(self):
        return self.dao.get_all()
    
    def listar_relatorio_pedidos(self, id):
        pedidos = (
            self.session.query(Orders)
            .options(
                joinedload(Orders.customers),
                joinedload(Orders.employees),
                joinedload(Orders.order_details)
                .joinedload(OrderDetails.products)
            )
            .filter(Orders.orderid == id)
            .first()  
        )
        return pedidos
    
    def listar_ranking_funcionarios(self, data_inicio, data_fim):
        query = (
            self.session.query(
                (Employees.titleofcourtesy + ' ' + Employees.firstname + ' ' + Employees.lastname).label("employee_name"),
                func.count(distinct(Orders.orderid)).label("total_orders"),
                func.sum(OrderDetails.quantity * OrderDetails.unitprice).label("total_sales")
            )
            .join(Employees, Orders.employeeid == Employees.employeeid)
            .join(OrderDetails, Orders.orderid == OrderDetails.orderid)
            .filter(Orders.orderdate.between(data_inicio, data_fim))
            .group_by(Employees.employeeid, Employees.titleofcourtesy, Employees.firstname, Employees.lastname)
            .order_by(func.sum(OrderDetails.quantity * OrderDetails.unitprice).desc())
        )

        return query.all()