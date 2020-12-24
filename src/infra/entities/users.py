from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.infra.config import Base


class Users(Base):
    """ Users Entity """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    id_pet = relationship("Pets")

    def __rep__(self):
        return f"Usr [name={self.name}]"
