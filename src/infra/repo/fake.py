# pylint: disable=E1101

from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class FakerRepo:
    """ A simple Repository """

    @classmethod
    def insert_use(cls):
        """ something """

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name="Programador", password="Lhama")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
