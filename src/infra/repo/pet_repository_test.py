from faker import Faker
from .pet_repository import PetRepository
from src.infra.config import DBConnectionHandler


faker = Faker()
pet_repository = PetRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_pet():
    """ Should insert pet in Pet table and return it """

    name = faker.name()
    specie = "fish"
    age = faker.random_number(digits=1)
    user_id = faker.random_number()

    # SQL Commands
    new_pet = pet_repository.insert_pet(name, specie, age, user_id)
    engine = db_connection_handler.get_engine()
    query_user = engine.execute(
        "SELECT * FROM pets WHERE id='{}';".format(new_pet.id)
    ).fetchone()

    assert new_pet.id == query_user.id
    assert new_pet.name == query_user.name
    assert new_pet.specie == query_user.specie
    assert new_pet.age == query_user.age
    assert new_pet.user_id == query_user.user_id

    engine.execute("DELETE FROM pets WHERE id='{}';".format(new_pet.id))
