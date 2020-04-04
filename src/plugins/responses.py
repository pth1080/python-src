from django.conf import settings
from django.http import JsonResponse
from django.utils.translation import activate
from django.utils.translation import gettext as _
from rest_framework import status


def ok(data, message="success", error_code=None):
    response = {
        'message': message,
        'data': data,
        'status': status.HTTP_200_OK
    }
    if error_code:
        response.update({
            'error': error_code
        })

    return JsonResponse(response, status=status.HTTP_200_OK)


def bad_request(data=None, message="error", error_code=None, request=None, message_code=None):
    if request and message_code:
        activate(settings.LANGUAGE_CODE)
        message = _(message_code)
    response = {
        'data': data,
        'status': status.HTTP_400_BAD_REQUEST,
        'message': message,
    }
    if error_code:
        response.update({
            'error_code': error_code
        })
    return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
