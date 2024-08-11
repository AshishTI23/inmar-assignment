from django.http import Http404
from django.shortcuts import _get_queryset


def get_object_or_404(klass, *args, **kwargs):
    """
    Retrieve an object from the database or raise Http404 with optional custom behavior.

    Parameters:
    - klass: The model class or queryset to query.
    - *args: Positional arguments for filtering the queryset.
    - **kwargs: Keyword arguments for filtering the queryset.

    Returns:
    - The retrieved object if it exists.

    Raises:
    - Http404: If the object does not exist.
    """
    queryset = _get_queryset(klass)
    try:
        # Try to retrieve the object based on provided filters.
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        # Construct the error message.
        response_dict = {
            "error": f"{klass.__name__} does not exist.",
            "success": False,
        }

        # Raise the Http404 exception with the error message.
        raise Http404(response_dict)
