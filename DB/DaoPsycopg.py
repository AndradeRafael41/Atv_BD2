import psycopg 
from psycopg.errors import OperationalError
from dotenv import load_dotenv
import os

class Connection:
    _connection = None

    load_dotenv()
    
    @staticmethod
    def connect():
        
        if Connection._connection is None:
            try:
                Connection._connection = psycopg.connect(
                    host=os.getenv("DB_HOST"),
                    port=os.getenv("DB_PORT"),
                    dbname=os.getenv("DB_NAME"),
                    user=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASSWORD"),
                    autocommit=True
                )
                
                print ("successfully connected to database")
            
            except OperationalError as E:
                print(f"Error connecting to database")
                raise
        
        return Connection._connection
    
    @staticmethod
    def close_connection():
        if Connection._connection  is not None:
            Connection._connection.close()
            print("Database connection closed")
            Connection._connection = None


