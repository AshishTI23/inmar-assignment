from rest_framework.pagination import PageNumberPagination

from base.http import SuccessResponse


class CustomPagination(PageNumberPagination):
    # Customize the default page size
    page_size = 10
    # Allow the client to set the page size via a query parameter
    page_size_query_param = "page_size"
    # Set a maximum page size to avoid potential abuse
    max_page_size = 30

    def get_paginated_response(self, data):
        return SuccessResponse(
            {
                "total_items": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "current_page": self.page.number,
                "next_page": self.get_next_link(),
                "previous_page": self.get_previous_link(),
                "results": data,
            }
        )
