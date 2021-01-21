from abc import ABC, abstractclassmethod
from typing import Dict, List
from src.domain.models import Users


class FindUser(ABC):
    """ Interface to FindPet use case """

    @abstractclassmethod
    def by_id(cls, user_id: int) -> Dict[bool, List[Users]]:
        """ Specific Case """

        raise Exception("Should implement method: by_id")

    @abstractclassmethod
    def by_name(cls, name: str) -> Dict[bool, List[Users]]:
        """ Specific Case """

        raise Exception("Should implement method: by_name")

    @abstractclassmethod
    def by_id_and_name(cls, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """ Specific Case """

        raise Exception("Should implement method: by_name")
