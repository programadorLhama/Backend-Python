from faker import Faker
from src.infra.test import PetRepositorySpy
from .find import FindPet

faker = Faker()


def test_by_pet_id():
    """ Testing pet_id method in FindPet """

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attibutes = {"pet_id": faker.random_number(digits=2)}
    response = find_pet.by_pet_id(pet_id=attibutes["pet_id"])

    # Testing Input
    assert pet_repo.select_pet_param["pet_id"] == attibutes["pet_id"]

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]
