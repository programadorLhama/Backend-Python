from typing import Type
from src.main.interface import RouteInterface
from src.domain.use_cases import FindUser
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class FindUserController(RouteInterface):
    """ Class to define controller to find_user use case """

    def __init__(self, find_user_use_case: Type[FindUser]):
        self.find_user_use_case = find_user_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ Method to call use case """

        response = None

        if http_request.query:
            # If query

            query_string_params = http_request.query.keys()

            if "user_id" in query_string_params and "user_name" in query_string_params:
                user_id = http_request.query["user_id"]
                user_name = http_request.query["user_name"]
                response = self.find_user_use_case.by_id_and_name(
                    user_id=user_id, name=user_name
                )

            elif (
                "user_id" in query_string_params
                and "user_name" not in query_string_params
            ):
                user_id = http_request.query["user_id"]
                response = self.find_user_use_case.by_id(user_id=user_id)

            elif (
                "user_id" not in query_string_params
                and "user_name" in query_string_params
            ):
                user_name = http_request.query["user_name"]
                response = self.find_user_use_case.by_name(name=user_name)

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        # If no query in http_request
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
