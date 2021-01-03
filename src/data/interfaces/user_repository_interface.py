from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Users


class UserRepositoryInterface(ABC):
    """ Interface to Pet Repository """

    @abstractmethod
    def insert_user(self, name: str, password: str) -> Users:
        """ abstractmethod  """

        raise Exception("Method not implemented")

    @abstractmethod
    def select_user(self, user_id: int = None, name: str = None) -> List[Users]:
        """ abstractmethod  """

        raise Exception("Method not implemented")
