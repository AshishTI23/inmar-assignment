from django.http import Http404
from django.http import JsonResponse
from django.http.response import JsonResponse


class SuccessResponse(JsonResponse):
    """
    A custom JsonResponse class to standardize successful API responses.

    Attributes:
    - data (optional): The data to be included in the response.
      If `data` is provided and is not an empty list, it will be included under the "data" key.
      If `data` is None or not an empty list, an empty dictionary will be used as the default value.
    - *args: Additional positional arguments passed to the JsonResponse class.
    - **kwargs: Additional keyword arguments passed to the JsonResponse class.

    Example Usage:
    - Standard success response with data:
        response = SuccessResponse(data={"key": "value"})
    - Success response with overridden status code:
        response = SuccessResponse(data={"key": "value"}, status=201)
    """

    def __init__(self, data=None, *args, **kwargs):
        # Ensuring the "data" field is populated with valid content or defaults to an empty dictionary.
        data = {"data": data if data or isinstance(data, list) else {}, "success": True}

        # Initialize the JsonResponse with the constructed data and any additional arguments.
        super(SuccessResponse, self).__init__(data, *args, **kwargs)


class ErrorResponse(JsonResponse):
    """
    A custom JsonResponse class to standardize error API responses.

    Attributes:
    - error (optional): A descriptive error message.
      If `error` is provided, it will be included under the "error" key.
      If `error` is not provided, a default error message will be used.
    - *args: Additional positional arguments passed to the JsonResponse class.
    - **kwargs: Additional keyword arguments passed to the JsonResponse class.
      If the "status" keyword argument is not provided, it defaults to 400 (Bad Request).

    Example Usage:
    - Standard error response with custom message:
        response = ErrorResponse(error="Invalid input data.")
    - Error response with default message and overridden status code:
        response = ErrorResponse(status=404)
    """

    def __init__(self, error=None, *args, **kwargs):
        # Setting the default status code to 400 if not explicitly provided.
        if not kwargs.get("status"):
            kwargs["status"] = 400

        # Construct the response data with the provided or default error message.
        data = {
            "error": error
            if error
            else "Error not provided but I assure you something went wrong!",
            "success": False,
        }

        # Initialize the JsonResponse with the constructed data and any additional arguments.
        super(ErrorResponse, self).__init__(data, *args, **kwargs)
