from typing import Dict, List, Type
from src.data.interfaces import PetRepositoryInterface as PetRepository
from src.domain.use_cases import FindPet as FindPetInterface
from src.domain.models import Pets


class FindPet(FindPetInterface):
    """ Class to define usecase: Find Pet """

    def __init__(self, pet_repository: Type[PetRepository]):
        self.pet_repository = pet_repository

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Select Pet By pet_id
        :param - pet_id: id of the pet
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id)

        return {"Success": validate_entry, "Data": response}

    def by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        """Select Pet By user_id
        :param - user_id: id of the user owne of the pet
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_pet_id_and_user_id(
        self, pet_id: int, user_id: int
    ) -> Dict[bool, List[Pets]]:
        """Select Pet By user_id
        :param - user_id: id of the user owne of the pet
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_id, int) and isinstance(pet_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id, user_id=user_id)

        return {"Success": validate_entry, "Data": response}
