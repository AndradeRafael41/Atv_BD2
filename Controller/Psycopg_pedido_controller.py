from DB.PsycopgDao import PsycopgGenericDAO
from Model.orders import Orders
from Model.costumers import Customers
from Model.employees import Employees
from Model.shippers import Shippers
from Model.products import Products
from Model.orderDetails import OrderDetails  # Importar o model OrderDetails
from DB.PsycopgConn import create_connection
import datetime
import decimal


class PedidoController:

    def __init__(self):
        # Inicializa os DAOs
        self.dao = PsycopgGenericDAO(Orders, 'orders', 'orderid', 'northwind')
        self.cliente_dao = PsycopgGenericDAO(Customers, 'customers', 'customerid', 'northwind')
        self.funcionario_dao = PsycopgGenericDAO(Employees, 'employees', 'employeeid', 'northwind')
        self.entregador_dao = PsycopgGenericDAO(Shippers, 'shippers', 'shipperid', 'northwind')
        self.produto_dao = PsycopgGenericDAO(Products, 'products', 'productid', 'northwind')
        self.order_details_dao = PsycopgGenericDAO(OrderDetails, 'order_details', 'orderid', 'northwind')  # DAO para order_details

        # Armazena o último pedido criado e seus itens
        self.ultimo_orderid = None
        self.itens_pedido = []

    def _gerar_orderid(self):
        query = "SELECT nextval('northwind.orders_id_sequence')"
        with create_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                result = cur.fetchone()
                return result[0]

    def criar_pedido(self, customerid, employeeid, shipperid, endereco, cidade, regiao, pais, cep, freight, requiredDate, shippedDate, shipName):
        orderid = self._gerar_orderid()  # Gera novo ID

        pedido = {
            'orderid': orderid,
            'customerid': customerid,
            'employeeid': employeeid,
            'orderdate': datetime.datetime.now(),
            'requireddate': requiredDate,
            'shippeddate': shippedDate,
            'freight': freight if isinstance(freight, decimal.Decimal) else decimal.Decimal(freight),
            'shipname': shipName,
            'shipaddress': endereco,
            'shipcity': cidade,
            'shipregion': regiao,
            'shippostalcode': cep,
            'shipcountry': pais,
            'shipperid': shipperid
        }

        self.dao.create(pedido)  # Cria o pedido
        self.ultimo_orderid = orderid  # Armazena o orderid do pedido criado
        self.itens_pedido = []  # Limpa itens anteriores (se houver)
        return orderid

    def adicionar_item_pedido(self, productid, unitprice, quantity, discount):
        if self.ultimo_orderid is None:
            raise Exception("Crie um pedido antes de adicionar itens.")

        item = {
            'orderid': self.ultimo_orderid,
            'productid': productid,
            'unitprice': unitprice if isinstance(unitprice, decimal.Decimal) else decimal.Decimal(unitprice),
            'quantity': quantity,
            'discount': discount if isinstance(discount, decimal.Decimal) else decimal.Decimal(discount)
        }

        self.itens_pedido.append(item)

    def salvar_itens_pedido(self):
        if not self.itens_pedido:
            raise Exception("Nenhum item para salvar.")

        for item in self.itens_pedido:
            self.order_details_dao.create(item)  # Salva cada item no OrderDetails

        # Limpa a lista após salvar
        self.itens_pedido = []

    # Métodos auxiliares
    def listar_clientes(self):
        return self.cliente_dao.get_all()

    def listar_funcionarios(self):
        return self.funcionario_dao.get_all()

    def listar_entregadores(self):
        return self.entregador_dao.get_all()

    def listar_produtos(self):
        return self.produto_dao.get_all()
