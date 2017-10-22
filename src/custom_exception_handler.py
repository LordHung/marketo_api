import logging
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    logger.exception(exc)

    if type(exc) == Exception:
        exc = APIException(detail=exc.message)

    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        # response.status_code = 200
        response.data['StatusCode'] = response.status_code
        response.data['Code'] = -1
        try:
            response.data['Code'] = exc.code
        except:
            pass

        try:
            response.data['Message'] = response.data.pop('detail', None)
        except:
            pass

    return response
