from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

class Database:
    def __init__(self):
        self._user = os.getenv("DB_USER")
        self._password = os.getenv("DB_PASSWORD")
        self._host = os.getenv("DB_HOST")
        self._port = os.getenv("DB_PORT")
        self._name = os.getenv("DB_NAME")

        self._url = (
            f"postgresql+psycopg2://{self._user}:{self._password}"
            f"@{self._host}:{self._port}/{self._name}"
        )

        self._engine = create_engine(self._url, echo=False)
        self._session_maker = sessionmaker(bind=self._engine, autocommit=False, autoflush=False)

    @property
    def session(self):
        return self._session_maker()

    @property
    def engine(self):
        return self._engine


    def close_connection(self):
        self._engine.dispose()
        print("connection to SQLAlchemy closed.")
