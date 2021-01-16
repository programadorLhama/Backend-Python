from faker import Faker
from src.infra.test import PetRepositorySpy
from .find import FindPet

faker = Faker()


def test_by_pet_id():
    """ Testing pet_id method in FindPet """

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attribute = {"pet_id": faker.random_number(digits=2)}
    response = find_pet.by_pet_id(pet_id=attribute["pet_id"])

    # Testing Input
    assert pet_repo.select_pet_param["pet_id"] == attribute["pet_id"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def test_fail_by_pet_id():
    """ Testing pet_id fail method in FindPet """

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attribute = {"pet_id": faker.word()}
    response = find_pet.by_pet_id(pet_id=attribute["pet_id"])

    # Testing Input
    assert pet_repo.select_pet_param == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_user_id():
    """ Testing by_id method in FindPet """

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attribute = {"user_id": faker.random_number(digits=2)}
    response = find_pet.by_user_id(user_id=attribute["user_id"])

    # Testing Input
    assert pet_repo.select_pet_param["user_id"] == attribute["user_id"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def test_fail_by_user_id():
    """ Testing by_id fail method in FindPet """

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attribute = {"user_id": faker.word()}
    response = find_pet.by_user_id(user_id=attribute["user_id"])

    # Testing Input
    assert pet_repo.select_pet_param == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_pet_id_and_user_id():
    """ Testing by_pet_id_and_user_id method in FindPet """

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attribute = {
        "user_id": faker.random_number(digits=2),
        "pet_id": faker.random_number(digits=2),
    }
    response = find_pet.by_pet_id_and_user_id(
        user_id=attribute["user_id"], pet_id=attribute["pet_id"]
    )

    # Testing Input
    assert pet_repo.select_pet_param["user_id"] == attribute["user_id"]
    assert pet_repo.select_pet_param["pet_id"] == attribute["pet_id"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def test_fail_by_pet_id_and_user_id():
    """ Testing by_pet_id_and_user_id fail method in FindPet """

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attribute = {"user_id": faker.word(), "pet_id": faker.word()}
    response = find_pet.by_pet_id_and_user_id(
        user_id=attribute["user_id"], pet_id=attribute["pet_id"]
    )

    # Testing Input
    assert pet_repo.select_pet_param == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None
