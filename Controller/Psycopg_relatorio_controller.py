from DB.PsycopgConn import create_connection

class RelatorioController:

    def __init__(self):
        # Inicializa o DAO e outras dependências conforme necessário
        pass

    def relatorio_pedidos(self, orderid):
        """
        Retorna os dados da view 'order_report' filtrados por 'orderid'.
        """
        query = """
        SELECT 
            ord.orderid AS order_number,
            ord.orderdate AS order_date,
            cust.companyname || ' - ' || cust.contactname AS customer_name,
            emp.titleofcourtesy || ' ' || emp.firstname || ' ' || emp.lastname AS employee_name,
            prd.productname AS product_name,
            ord_dt.quantity AS product_quantity,
            ord_dt.unitprice AS product_price
        FROM northwind.orders ord 
        INNER JOIN northwind.customers cust ON ord.customerid = cust.customerid 
        INNER JOIN northwind.employees emp ON ord.employeeid = emp.employeeid
        INNER JOIN northwind.order_details ord_dt ON ord.orderid = ord_dt.orderid
        INNER JOIN northwind.products prd ON ord_dt.productid = prd.productid
        WHERE ord.orderid = %s;
        """

        try:
            with create_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (orderid,))  # Passa o orderid como parâmetro
                    resultado = cursor.fetchall()  # Pega todos os resultados
                    return resultado

        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")
            return None

    def ranking_funcionarios (self, data_inicio, data_fim):
            """
            Retorna o ranking de vendas dos funcionários com base no intervalo de datas informado.
            """
            query = """
            SELECT 
                emp.titleofcourtesy || ' ' || emp.firstname || ' ' || emp.lastname AS employee_name,
                COUNT(DISTINCT ord.orderid) AS total_orders,
                SUM(ord_dt.quantity * ord_dt.unitprice) AS total_sales
            FROM 
                northwind.orders ord
                INNER JOIN northwind.employees emp ON ord.employeeid = emp.employeeid
                INNER JOIN northwind.order_details ord_dt ON ord.orderid = ord_dt.orderid
            WHERE 
                ord.orderdate BETWEEN %s AND %s
            GROUP BY 
                emp.employeeid
            ORDER BY 
                total_sales DESC;
            """

            try:
                with create_connection() as conn:
                    with conn.cursor() as cursor:
                        cursor.execute(query, (data_inicio, data_fim))
                        resultado = cursor.fetchall()
                        colunas = [desc[0] for desc in cursor.description]
                        return colunas, resultado

            except Exception as e:
                print(f"Erro ao buscar ranking de vendas: {e}")
                return None, None