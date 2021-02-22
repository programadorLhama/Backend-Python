from typing import Type
from sqlalchemy.exc import IntegrityError
from src.main.interface import RouteInterface as Route
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


def flask_adapter(request: any, api_route: Type[Route]) -> any:
    """Adapter pattern to Flask
    :param - Flask Request
    :api_route: Composite Routes
    """

    try:
        query_string_params = request.args.to_dict()

        if "pet_id" in query_string_params.keys():
            query_string_params["pet_id"] = int(query_string_params["pet_id"])

        if "user_id" in query_string_params.keys():
            query_string_params["user_id"] = int(query_string_params["user_id"])
    except:
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    http_request = HttpRequest(
        header=request.headers, body=request.json, query=query_string_params
    )

    try:
        response = api_route.route(http_request)
    except IntegrityError:
        http_error = HttpErrors.error_409()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
    except Exception as exc:
        print(exc)
        http_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    return response
