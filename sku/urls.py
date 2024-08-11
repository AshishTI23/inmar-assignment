from django.urls import path

from sku.views import CategoriesAPIView
from sku.views import DepartmentsAPIView
from sku.views import LocationsAPIView
from sku.views import StockKeepingUnitAPIView
from sku.views import SubCategoriesAPIView

urlpatterns = [
    # List all locations or create a new location
    path("api/v1/locations", LocationsAPIView.as_view(), name="locations"),
    # Update, or delete a specific location by its UUID
    path(
        "api/v1/locations/<uuid:location_id>",
        LocationsAPIView.as_view(),
        name="locations",
    ),
    # List all departments at a specific location by location UUID
    path(
        "api/v1/locations/<uuid:department>/departments",
        DepartmentsAPIView.as_view(),
        name="departments_at_location",
    ),
    # Update, or delete a specific department by its UUID
    path(
        "api/v1/departments/<uuid:department_id>",
        DepartmentsAPIView.as_view(),
        name="categories",
    ),
    # List all categories within a specific department at a given location
    path(
        "api/v1/locations/<uuid:location_id>/departments/<uuid:department_id>/categories",
        CategoriesAPIView.as_view(),
        name="categories_at_department",
    ),
    # Update, or delete a specific category by its UUID
    path(
        "api/v1/categories/<uuid:category_id>",
        CategoriesAPIView.as_view(),
        name="categories",
    ),
    # List all subcategories within a specific category in a given department and location
    path(
        "api/v1/locations/<uuid:location_id>/departments/<uuid:department_id>/categories/<uuid:category_id>/sub_categories",
        SubCategoriesAPIView.as_view(),
        name="sub_categories_for_category",
    ),
    # Update, or delete a specific subcategory by its UUID
    path(
        "api/v1/subcategories/<uuid:subcategory_id>",
        SubCategoriesAPIView.as_view(),
        name="subcategories",
    ),
    # List all SKUs or create a new SKU
    path("api/v1/skus", StockKeepingUnitAPIView.as_view(), name="skus"),
]
