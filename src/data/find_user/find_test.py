from faker import Faker
from src.infra.test import UserRepositorySpy
from .find import FindUser

faker = Faker()


def test_by_id():
    """ Testing by_id method in FindUser """

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attribute = {"id": faker.random_number(digits=2)}
    response = find_user.by_id(user_id=attribute["id"])

    # Testing Input
    assert user_repo.select_user_params["user_id"] == attribute["id"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def test_fail_by_id():
    """ Testing by_id fail method in FindUser """

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attribute = {"id": faker.word()}
    response = find_user.by_id(user_id=attribute["id"])

    # Testing Input
    assert user_repo.select_user_params == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_name():
    """ Testing by_name method in FindUser """

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attribute = {"name": faker.word()}
    response = find_user.by_name(name=attribute["name"])

    # Testing Input
    assert user_repo.select_user_params["name"] == attribute["name"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def test_fail_by_name():
    """ Testing by_name fail method in FindUser """

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attribute = {"name": faker.random_number(digits=2)}
    response = find_user.by_name(name=attribute["name"])

    # Testing Input
    assert user_repo.select_user_params == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_id_and_name():
    """ Testing by_id_and_name method in FindUser """

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attribute = {"user_id": faker.random_number(digits=2), "name": faker.word()}

    response = find_user.by_id_and_name(
        user_id=attribute["user_id"], name=attribute["name"]
    )

    # Testing Input
    assert user_repo.select_user_params["user_id"] == attribute["user_id"]
    assert user_repo.select_user_params["name"] == attribute["name"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def test_fail_by_id_and_name():
    """ Testing by_id_and_name fail method in FindUser """

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attribute = {
        "user_id": faker.random_number(digits=2),
        "name": faker.random_number(digits=2),
    }

    response = find_user.by_id_and_name(
        user_id=attribute["user_id"], name=attribute["name"]
    )

    # Testing Input
    assert user_repo.select_user_params == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None
