from django.urls import path

from sku.views import CategoriesAPIView
from sku.views import DepartmentsAPIView
from sku.views import LocationsAPIView
from sku.views import StockKeepingUnitAPIView
from sku.views import SubCategoriesAPIView

urlpatterns = [
    path("api/v1/locations", LocationsAPIView.as_view(), name="locations"),
    path(
        "api/v1/locations/<uuid:location_id>/departments",
        DepartmentsAPIView.as_view(),
        name="departments_at_location",
    ),
    path(
        "api/v1/locations/<uuid:location_id>/departments/<uuid:department_id>/categories",
        CategoriesAPIView.as_view(),
        name="categories_at_department",
    ),
    path(
        "api/v1/locations/<uuid:location_id>/departments/<uuid:department_id>/categories/<uuid:category_id>/sub_categories",
        SubCategoriesAPIView.as_view(),
        name="sub_categories_for_category",
    ),
]
