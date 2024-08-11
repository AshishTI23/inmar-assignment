from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from sku.models import Category
from sku.models import Department
from sku.models import Location
from sku.models import StockKeepingUnit
from sku.models import SubCategory


class LocationsAPITestCase(APITestCase):
    def setUp(self):
        self.location = Location.objects.create(name="Test Location")

    def test_get_locations(self):
        url = reverse("locations")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_location(self):
        url = reverse("locations")
        data = {"name": "New Location"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_location(self):
        url = reverse("locations", args=[self.location.id])
        data = {"name": "Updated Location"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_location(self):
        url = reverse("locations", args=[self.location.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class DepartmentsAPITestCase(APITestCase):
    def setUp(self):
        self.location = Location.objects.create(name="Test Location")
        self.department = Department.objects.create(
            name="Test Department", location=self.location
        )

    def test_get_departments_at_location(self):
        url = reverse("departments_at_location", args=[self.location.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_create_department(self):
    #     # FIXME: request.data["location"] = str(location_id)
    #     # AttributeError("This QueryDict instance is immutable")
    #     url = reverse('departments_at_location', args=[self.location.id])
    #     data = {"name": "New Department", "location": self.location.id}
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_department(self):
        url = reverse("departments", args=[self.department.id])
        data = {"name": "Updated Department"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_department(self):
        url = reverse("departments", args=[self.department.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CategoriesAPITestCase(APITestCase):
    def setUp(self):
        self.location = Location.objects.create(name="Test Location")
        self.department = Department.objects.create(
            name="Test Department", location=self.location
        )
        self.category = Category.objects.create(
            name="Test Category", department=self.department
        )

    def test_get_categories_at_department(self):
        url = reverse(
            "categories_at_department", args=[self.location.id, self.department.id]
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_create_category(self):
    #     # FIXME: request.data["location"] = str(location_id)
    #     # AttributeError("This QueryDict instance is immutable")
    #     url = reverse('categories_at_department', args=[self.location.id, self.department.id])
    #     data = {"name": "New Category", "department": str(self.department.id)}
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_category(self):
        url = reverse("categories", args=[self.category.id])
        data = {"name": "Updated Category"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_category(self):
        url = reverse("categories", args=[self.category.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SubCategoriesAPITestCase(APITestCase):
    def setUp(self):
        self.location = Location.objects.create(name="Test Location")
        self.department = Department.objects.create(
            name="Test Department", location=self.location
        )
        self.category = Category.objects.create(
            name="Test Category", department=self.department
        )
        self.subcategory = SubCategory.objects.create(
            name="Test SubCategory", category=self.category
        )

    def test_get_subcategories_for_category(self):
        url = reverse(
            "sub_categories_for_category",
            args=[self.location.id, self.department.id, self.category.id],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_create_subcategory(self):
    #     # FIXME: request.data["location"] = str(location_id)
    #     # AttributeError("This QueryDict instance is immutable")
    #     url = reverse('sub_categories_for_category', args=[self.location.id, self.department.id, self.category.id])
    #     data = {"name": "New SubCategory", "category": str(self.category.id)}
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_subcategory(self):
        url = reverse("subcategories", args=[self.subcategory.id])
        data = {"name": "Updated SubCategory"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_subcategory(self):
        url = reverse("subcategories", args=[self.subcategory.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class StockKeepingUnitAPITestCase(APITestCase):
    def setUp(self):
        self.location = Location.objects.create(name="Test Location")
        self.department = Department.objects.create(
            name="Test Department", location=self.location
        )
        self.category = Category.objects.create(
            name="Test Category", department=self.department
        )
        self.subcategory = SubCategory.objects.create(
            name="Test SubCategory", category=self.category
        )
        self.sku = StockKeepingUnit.objects.create(
            name="Test SKU", sku_code="12345", subcategory=self.subcategory
        )

    def test_get_skus(self):
        url = reverse("skus")
        query_params = {
            "location": "Test Location",
            "department": "Test Department",
            "category": "Test Category",
            "sub_category": "Test SubCategory",
        }
        response = self.client.get(url, query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
