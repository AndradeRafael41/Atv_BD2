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


class PedidoControllerDriver:

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

    def _gerar_orderid(self):
        query = "SELECT nextval('northwind.orders_id_sequence')"
        with create_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                result = cur.fetchone()
                return result[0]

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

        for detail in order_details:
            item = {
                'orderid': self.ultimo_orderid,
                'productid': detail.productid,
                'unitprice': detail.unitprice if isinstance(detail.unitprice, decimal.Decimal) else decimal.Decimal(detail.unitprice),
                'quantity': detail.quantity,
                'discount': detail.discount if isinstance(detail.discount, decimal.Decimal) else decimal.Decimal(detail.discount)
            }
            self.order_details_dao.create(item)  # Salva cada item no OrderDetails

    # Métodos auxiliares
    def listar_clientes(self):
        return self.cliente_dao.get_all()

    def listar_funcionarios(self):
        return self.funcionario_dao.get_all()

    def listar_entregadores(self):
        return self.entregador_dao.get_all()

    def listar_produtos(self):
        return self.produto_dao.get_all()
