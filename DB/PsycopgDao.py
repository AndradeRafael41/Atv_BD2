import psycopg2
from DB.PsycopgConn import create_connection
from typing import List, Optional

class PsycopgGenericDAO:
    def __init__(self, model_class, table_name, pk, schema):
        self.model_class = model_class
        self.table_name = table_name
        self.pk = pk
        self.schema = schema

    def _get_connection(self):
        """
        Obtém a conexão com o banco de dados.
        """
        return create_connection()

    def create(self, data: dict) -> Optional[object]:
        """
        Cria um registro na tabela especificada.
        """
        conn = self._get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                # Gerando os campos e valores para a query de inserção
                columns = ', '.join(data.keys())
                values = ', '.join([f"%s" for _ in data.values()])
                query = f"INSERT INTO {self.schema}.{self.table_name} ({columns}) VALUES ({values}) RETURNING {self.pk};"
                cursor.execute(query, tuple(data.values()))
                conn.commit()
                result = cursor.fetchone()
                cursor.close()
                return self.model_class(**dict(zip(data.keys(), result)))
            except Exception as e:
                print(f"Erro ao criar registro: {e}")
                return None
            finally:
                conn.close()
        return None

    def get_by_id(self, id_value: int) -> Optional[object]:
        """
        Obtém um registro por seu ID.
        """
        conn = self._get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = f"SELECT * FROM {self.schema}.{self.table_name} WHERE {self.pk} = %s;"
                cursor.execute(query, (id_value,))
                result = cursor.fetchone()
                cursor.close()
                if result:
                    return self.model_class(**dict(zip([desc[0] for desc in cursor.description], result)))
                return None
            except Exception as e:
                print(f"Erro ao buscar registro: {e}")
                return None
            finally:
                conn.close()
        return None

    def get_all(self) -> List[object]:
        """
        Obtém todos os registros da tabela.
        """
        conn = self._get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = f"SELECT * FROM {self.schema}.{self.table_name};"
                cursor.execute(query)
                result = cursor.fetchall()
                cursor.close()
                return [self.model_class(**dict(zip([desc[0] for desc in cursor.description], row))) for row in result]
            except Exception as e:
                print(f"Erro ao buscar todos os registros: {e}")
                return []
            finally:
                conn.close()
        return []

    def update(self, id_value: int, data: dict) -> Optional[object]:
        """
        Atualiza um registro existente.
        """
        conn = self._get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                set_clause = ', '.join([f"{key} = %s" for key in data.keys()])
                query = f"UPDATE {self.schema}.{self.table_name} SET {set_clause} WHERE {self.pk} = %s RETURNING {self.pk};"
                cursor.execute(query, tuple(data.values()) + (id_value,))
                conn.commit()
                result = cursor.fetchone()
                cursor.close()
                return self.model_class(**dict(zip(data.keys(), result)))
            except Exception as e:
                print(f"Erro ao atualizar registro: {e}")
                return None
            finally:
                conn.close()
        return None

    def delete(self, id_value: int) -> bool:
        """
        Exclui um registro da tabela.
        """
        conn = self._get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = f"DELETE FROM {self.schema}.{self.table_name} WHERE {self.pk} = %s;"
                cursor.execute(query, (id_value,))
                conn.commit()
                cursor.close()
                return True
            except Exception as e:
                print(f"Erro ao excluir registro: {e}")
                return False
            finally:
                conn.close()
        return False
