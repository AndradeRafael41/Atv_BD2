from DB.DaoOrm import GenericDAO, SessionLocal
from Model.orders import Orders
from Model.costumers import Customers
from Model.employees import Employees
from Model.shippers import Shippers
from Model.products import Products
import datetime

class PedidoController:

    def __init__(self):
        self.session = SessionLocal()
        self.dao = GenericDAO(self.session, Orders)
        self.cliente_dao = GenericDAO(self.session, Customers)
        self.funcionario_dao = GenericDAO(self.session, Employees)
        self.entregador_dao = GenericDAO(self.session, Shippers)
        self.produto_dao = GenericDAO(self.session, Products)

    def criar_pedido(
        self,
        customerid,
        employeeid,
        shipperid,
        endereco,
        cidade,
        regiao,
        pais,
        cep,
        freight,
        requiredDate,
        shippedDate,
        shipName,
        order_details
    ):
        novo_pedido = Orders(
            customerid = customerid,
            employeeid = employeeid,
            orderdate = datetime.datetime.now(),
            requireddate = requiredDate,
            shippeddate = shippedDate,
            freight = freight,
            shipname = shipName,
            shipaddress = endereco,
            shipcity = cidade,
            shipregion = regiao,
            shippostalcode = cep,
            shipcountry = pais,
            shipperid = shipperid,
            order_details = order_details
        )
        self.dao.add(novo_pedido)


    def listar_clientes(self):
        return self.cliente_dao.get_all()

    def listar_funcionarios(self):
        return self.funcionario_dao.get_all()

    def listar_entregadores(self):
        return self.entregador_dao.get_all()
    def listar_produtos(self):
        return self.produto_dao.get_all()
