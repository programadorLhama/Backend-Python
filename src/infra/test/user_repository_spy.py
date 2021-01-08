from typing import List
from src.domain.models import Users
from src.domain.test import mock_users


class UserRepositorySpy:
    """ Spy to User Repository """

    def __init__(self):
        self.insert_user_params = {}
        self.select_user_params = {}

    def insert_user(self, name: str, password: str) -> Users:
        """ Spy to all the attributes """

        self.insert_user_params["name"] = name
        self.insert_user_params["password"] = password

        return mock_users()

    def select_user(self, user_id: int = None, name: str = None) -> List[Users]:
        """ Spy to all the attributes """

        self.select_user_params["user_id"] = user_id
        self.select_user_params["name"] = name

        return [mock_users()]
