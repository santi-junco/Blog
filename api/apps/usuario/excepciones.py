from rest_framework.exceptions import APIException

class ErrorReguistro(APIException):
    status_code = 400
    default_detail = 'Verifique que se enviaron los campos "Nombre", "Apellido", "Email" y "Password"'
    default_code = 'Falta_informacion'
