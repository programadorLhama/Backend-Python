from typing import Dict, List
from src.domain.models import Users, Pets
from src.domain.test import mock_pet, mock_users


class RegisterPetSpy:
    """ Class to define usecase: Register Pet """

    def __init__(self, pet_repository: any, find_user: any):
        self.pet_repository = pet_repository
        self.find_user = find_user
        self.registry_param = {}

    def registry(
        self, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """ Registry pet """

        self.registry_param["name"] = name
        self.registry_param["specie"] = specie
        self.registry_param["age"] = age
        self.registry_param["user_information"] = user_information

        response = None

        # Validating entry and trying to find an user
        validate_entry = isinstance(name, str) and isinstance(specie, str)
        user = self.__find_user_information(user_information)
        checker = validate_entry and user["Success"]

        if checker:
            response = mock_pet()

        return {"Success": checker, "Data": response}

    @classmethod
    def __find_user_information(
        cls, user_information: Dict[int, str]
    ) -> Dict[bool, List[Users]]:
        """ Check userInfo Dicionaty and select user """

        user_founded = None
        user_params = user_information.keys()

        if "user_id" and "user_name" in user_params:
            # find user by id and name
            user_founded = {"Success": True, "Data": mock_users()}

        elif "user_name" not in user_params and "user_id" in user_params:
            # find user by id
            user_founded = {"Success": True, "Data": mock_users()}

        elif "user_id" not in user_params and "user_name" in user_params:
            # find user by name
            user_founded = {"Success": True, "Data": mock_users()}

        else:
            return {"Success": False, "Data": None}

        return user_founded
