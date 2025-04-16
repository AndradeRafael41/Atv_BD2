from DB.DaoOrm import GenericDAO, SessionLocal
from Model.orders import Orders
from Model.costumers import Customers
from Model.employees import Employees
from Model.shippers import Shippers
from Model.products import Products
from Model.orderDetails import OrderDetails
from sqlalchemy import func, distinct
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
    
    def listar_relatorio_pedidos(self):
        query = (
            self.session.query(
                Orders.orderid.label("order_number"),
                Orders.orderdate.label("order_date"),
                (Customers.companyname + ' - ' + Customers.contactname).label("customer_name"),
                (Employees.titleofcourtesy + ' ' + Employees.firstname + ' ' + Employees.lastname).label("employee_name"),
                Products.productname.label("product_name"),
                OrderDetails.quantity.label("product_quantity"),
                OrderDetails.unitprice.label("product_price")
            )
            .join(Customers, Orders.customerid == Customers.customerid)
            .join(Employees, Orders.employeeid == Employees.employeeid)
            .join(OrderDetails, Orders.orderid == OrderDetails.orderid)
            .join(Products, OrderDetails.productid == Products.productid)
        )

        result = query.all() 
        return result
    
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

# Execução
relat = RelatorioController()

# Chama o método da instância
result = relat.listar_relatorio_pedidos()

# Converte os objetos Row para dicionários
dados_formatados = [dict(r._mapping) for r in result]

# Imprime formatado como tabela
print(tabulate(dados_formatados, headers="keys", tablefmt="grid"))


#ata_inicio = datetime.datetime.strptime("19-08-1994", "%d-%m-%Y").date()
#data_fim = datetime.datetime.strptime("05-09-1994", "%d-%m-%Y").date()

# Chama o método da instância
#result = relat.listar_ranking_funcionarios(data_inicio,data_fim)

# Converte os objetos Row para dicionários
#dados_formatados = [dict(r._mapping) for r in result]

# Imprime formatado como tabela
#print(tabulate(dados_formatados, headers="keys", tablefmt="grid"))
