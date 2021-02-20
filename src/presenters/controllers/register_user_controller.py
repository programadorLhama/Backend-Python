from typing import Type
from src.main.interface import RouteInterface
from src.domain.use_cases import RegisterUser
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class RegisterUserController(RouteInterface):
    """ Class to Define Route to register_user use case """

    def __init__(self, register_user_use_case: Type[RegisterUser]):
        self.register_user_use_case = register_user_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ Method to call use case """

        response = None

        if http_request.body:
            # if body in htp_request

            body_params = http_request.body.keys()

            if "name" in body_params and "password" in body_params:
                name = http_request.body["name"]
                password = http_request.body["password"]
                response = self.register_user_use_case.register(
                    name=name, password=password
                )

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                https_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=https_error["status_code"], body=https_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        # If no body in http_request
        https_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )
