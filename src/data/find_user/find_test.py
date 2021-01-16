from faker import Faker
from .find import FindUser
from src.infra.test import UserRepositorySpy

faker = Faker()


def test_by_id():
    """ Testing by_id method """

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"id": faker.random_number(digits=2)}
    response = find_user.by_id(user_id=attributes["id"])

    # Testing Inputs
    assert user_repo.select_user_params["user_id"] == attributes["id"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]
