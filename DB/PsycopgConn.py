import psycopg2
import os
from psycopg2 import sql
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
load_dotenv()

# Função para criar a conexão
def create_connection():
    """
    Cria e retorna uma conexão com o banco de dados.
    """
    try:
        # Lendo variáveis do ambiente
        host = os.getenv('DB_HOST')
        dbname = os.getenv('DB_NAME')
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        port = os.getenv('DB_PORT')  

        
        connection = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password,
            port=port
        )
        
        print("Conexão bem-sucedida!")
        return connection

    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def test_connection():
    """
    Função para testar a conexão com o banco de dados.
    """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT 1;")  
            print("Conexão de teste bem-sucedida!")
            cursor.close()
        except Exception as e:
            print(f"Erro ao testar a conexão: {e}")
        finally:
            connection.close()
    else:
        print("Não foi possível conectar ao banco.")

test_connection()