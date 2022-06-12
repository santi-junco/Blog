from rest_framework.exceptions import APIException

class Error(APIException):
    status_code = 400
    default_detail = 'Error'
    default_code = 'Error'

    def __init__(self, error='Error al procesar la solicitud', cod=400):
        self.default_detail = error
        self.status_code = cod
        super().__init__()