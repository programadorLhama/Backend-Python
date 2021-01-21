from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import Pets


class FindPet(ABC):
    """ Interface to FindPet use case """

    @abstractmethod
    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """ Specific case """

        raise Exception("Should implement method: by_pet_id")

    @abstractmethod
    def by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        """ Specific case """

        raise Exception("Should implement method: by_user_id")

    @abstractmethod
    def by_pet_id_and_user_id(
        self, pet_id: int, user_id: int
    ) -> Dict[bool, List[Pets]]:
        """ Specific case """

        raise Exception("Should implement method: by_pet_id_and_user_id")
