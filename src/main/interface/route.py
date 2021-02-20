from typing import Type
from abc import ABC, abstractmethod
from src.presenters.helpers import HttpRequest, HttpResponse


class RouteInterface(ABC):
    """ Interface to Routes """

    @abstractmethod
    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ Defining Route """

        raise Exception("Should implement method: route")
