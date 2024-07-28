
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if response.status_code == 401:
            response.data = {
                'detail': 'Токен не действителен или истек. Пожалуйста, получите новый токен.'
            }

    return response
