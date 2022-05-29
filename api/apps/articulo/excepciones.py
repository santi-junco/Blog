from rest_framework.exceptions import APIException

class ErrorImagen(APIException):
    status_code = 400
    default_detail = 'No se puede agregar la imagen'
    default_code = 'Error_Imagen'