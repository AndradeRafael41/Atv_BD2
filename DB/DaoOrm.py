from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generic, TypeVar, Type, List, Optional
from sqlalchemy.orm import Session

from dotenv import load_dotenv
import os

load_dotenv()
T = TypeVar('T')


DATABASE_URL = (
            f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
            f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
        )

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)


class GenericDAO(Generic[T]):
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    def get_by_id(self, id_: int) -> Optional[T]:
        return self.session.get(self.model, id_)

    def get_all(self) -> List[T]:
        return self.session.query(self.model).all()

    def add(self, obj: T) -> None:
        try:
            self.session.add(obj)
            self.session.commit()
        except:
            self.session.rollback()
            raise

    def update(self, obj: T) -> None:
        try:
            self.session.merge(obj)
            self.session.commit()
        except:
            self.session.rollback()
            raise

    def delete(self, obj: T) -> None:
        try:
            self.session.delete(obj)
            self.session.commit()
        except:
            self.session.rollback()
            raise
