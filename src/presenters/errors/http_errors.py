class HttpErrors:
    """ Class to define errors in http """

    @staticmethod
    def error_422():
        """ HTTP 422 """

        return {"status_code": 422, "body": {"error": "Unprocessable Entirty"}}

    @staticmethod
    def error_400():
        """ HTTP 400 """

        return {"status_code": 400, "body": {"error": "Bad Request"}}

    @staticmethod
    def error_409():
        """ HTTP 409 """

        return {"status_code": 409, "body": {"error": "Conflict"}}

    @staticmethod
    def error_500():
        """ HTTP 500 """

        return {"status_code": 500, "body": {"error": "Internal Server Error"}}
