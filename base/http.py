from django.http import Http404
from django.http.response import JsonResponse
from django.shortcuts import _get_queryset


class SuccessResponse(JsonResponse):
    def __init__(self, data=None, *args, **kwargs):
        data = {"data": data if data or isinstance(data, list) else {}, "success": True}
        super(SuccessResponse, self).__init__(data, *args, **kwargs)
        # If we want to override the status code then return response
        # SuccessResponse(data, status=201)


class ErrorResponse(JsonResponse):
    def __init__(self, error=None, *args, **kwargs):
        if not kwargs.get("status"):
            # Default status is 200 in JsonResponse class
            kwargs["status"] = 400
        data = {
            "error": error
            if error
            else "Error not provided but I assure you something went wrong!",
            "success": False,
        }
        super(ErrorResponse, self).__init__(data, *args, **kwargs)
