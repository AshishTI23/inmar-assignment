import uuid

from rest_framework import status
from rest_framework.views import APIView

from base.generics import get_object_or_404
from base.http import ErrorResponse
from base.http import SuccessResponse
from sku.models import Category
from sku.models import Department
from sku.models import Location
from sku.models import StockKeepingUnit
from sku.models import SubCategory
from sku.serializers import CategorySerializer
from sku.serializers import DepartmentSerializer
from sku.serializers import LocationSerializer
from sku.serializers import SKUQueryParamsSerializer
from sku.serializers import StockKeepingUnitSerializer
from sku.serializers import SubCategorySerializer


class LocationsAPIView(APIView):
    """
    API view for handling requests related to Location models.
    """

    def get(self, request):
        """
        Retrieve a list of all Location instances.

        Args:
            request: The HTTP request object.

        Returns:
            SuccessResponse: A response containing a list of all Location instances.
        """
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return SuccessResponse(serializer.data)

    def post(self, request):
        """
        Create a new Location instance.

        Args:
            request: The HTTP request object containing the Location data.

        Returns:
            SuccessResponse: A response containing the created Location instance.
            ErrorResponse: A response containing validation errors if the data is invalid.
        """
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return ErrorResponse(serializer.errors)

    def patch(self, request, location_id):
        """
        Update an existing Location instance partially.

        Args:
            request: The HTTP request object containing the update data.
            location_id: The ID of the Location instance to update.

        Returns:
            SuccessResponse: A response containing the updated Location instance.
            ErrorResponse: A response containing validation errors if the data is invalid.
        """
        location_instance = get_object_or_404(Location, id=location_id)
        serializer = LocationSerializer(
            instance=location_instance, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(serializer.data)
        else:
            return ErrorResponse(serializer.errors)

    def delete(self, request, location_id):
        """
        Delete a Location instance.

        Args:
            request: The HTTP request object.
            location_id: The ID of the Location instance to delete.

        Returns:
            SuccessResponse: A response indicating successful deletion.
        """
        location_instance = get_object_or_404(Location, id=location_id)
        location_instance.delete()
        return SuccessResponse(status=status.HTTP_204_NO_CONTENT)


class DepartmentsAPIView(APIView):
    """
    API view for handling requests related to Department models.
    """

    def get(self, request, location_id):
        """
        Retrieve a list of all Departments for a specific location.

        Args:
            request: The HTTP request object.
            location_id: The ID of the Location instance to filter Departments.

        Returns:
            SuccessResponse: A response containing a list of all Department instances for the specified location.
        """
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return SuccessResponse(serializer.data)

    def post(self, request, location_id):
        """
        Create a new Department instance within a specific location.

        Args:
            request: The HTTP request object containing the Department data.
            location_id: The ID of the Location instance where the Department will be created.

        Returns:
            SuccessResponse: A response containing the created Department instance.
            ErrorResponse: A response containing validation errors if the data is invalid.
        """
        request_body = request.data
        request_body["location"] = str(location_id)
        serializer = DepartmentSerializer(data=request_body)
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return ErrorResponse(serializer.errors)

    def patch(self, request, department_id):
        """
        Update an existing Department instance partially.

        Args:
            request: The HTTP request object containing the update data.
            department_id: The ID of the Department instance to update.

        Returns:
            SuccessResponse: A response containing the updated Department instance.
            ErrorResponse: A response containing validation errors if the data is invalid.
        """
        department_instance = get_object_or_404(Department, id=department_id)
        serializer = DepartmentSerializer(
            instance=department_instance, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(serializer.data)
        else:
            return ErrorResponse(serializer.errors)

    def delete(self, request, department_id):
        """
        Delete a Department instance.

        Args:
            request: The HTTP request object.
            department_id: The ID of the Department instance to delete.

        Returns:
            SuccessResponse: A response indicating successful deletion.
        """
        department_instance = get_object_or_404(Department, id=department_id)
        department_instance.delete()
        return SuccessResponse(status=status.HTTP_204_NO_CONTENT)


class CategoriesAPIView(APIView):
    """
    API view for handling requests related to Category models.
    """

    def get(self, request, location_id, department_id):
        """
        Retrieve a list of all Category instances for a specific location and department.

        Args:
            request: The HTTP request object.
            location_id: The ID of the Location instance to filter Categories.
            department_id: The ID of the Department instance to filter Categories.

        Returns:
            SuccessResponse: A response containing a list of all Category instances for the specified location and department.
        """
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return SuccessResponse(serializer.data)

    def post(self, request, location_id, department_id):
        """
        Create a new Category instance within a specific location and department.

        Args:
            request: The HTTP request object containing the Category data.
            location_id: The ID of the Location instance where the Category will be created.
            department_id: The ID of the Department instance where the Category will be created.

        Returns:
            SuccessResponse: A response containing the created Category instance.
            ErrorResponse: A response containing validation errors if the data is invalid.
        """
        request.data["location"] = str(location_id)
        request.data["department"] = str(department_id)
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return ErrorResponse(serializer.errors)

    def patch(self, request, category_id):
        """
        Update an existing Category instance partially.

        Args:
            request: The HTTP request object containing the update data.
            category_id: The ID of the Category instance to update.

        Returns:
            SuccessResponse: A response containing the updated Category instance.
            ErrorResponse: A response containing validation errors if the data is invalid.
        """
        category_instance = get_object_or_404(Category, id=category_id)
        serializer = CategorySerializer(
            instance=category_instance, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(serializer.data)
        else:
            return ErrorResponse(serializer.errors)

    def delete(self, request, category_id):
        """
        Delete a Category instance.

        Args:
            request: The HTTP request object.
            category_id: The ID of the Category instance to delete.

        Returns:
            SuccessResponse: A response indicating successful deletion.
        """
        category_instance = get_object_or_404(Category, id=category_id)
        category_instance.delete()
        return SuccessResponse(status=status.HTTP_204_NO_CONTENT)


class SubCategoriesAPIView(APIView):
    """
    API view for handling requests related to SubCategory models.
    """

    def get(self, request, location_id, department_id, category_id):
        """
        Retrieve a list of all SubCategory instances for a specific location, department, and category.

        Args:
            request: The HTTP request object.
            location_id: The ID of the Location instance to filter SubCategories.
            department_id: The ID of the Department instance to filter SubCategories.
            category_id: The ID of the Category instance to filter SubCategories.

        Returns:
            SuccessResponse: A response containing a list of all SubCategory instances for the specified location, department, and category.
        """
        subcategories = SubCategory.objects.all()
        serializer = SubCategorySerializer(subcategories, many=True)
        return SuccessResponse(serializer.data)

    def post(self, request, location_id, department_id, category_id):
        """
        Create a new SubCategory instance within a specific location, department, and category.

        Args:
            request: The HTTP request object containing the SubCategory data.
            location_id: The ID of the Location instance where the SubCategory will be created.
            department_id: The ID of the Department instance where the SubCategory will be created.
            category_id: The ID of the Category instance where the SubCategory will be created.

        Returns:
            SuccessResponse: A response containing the created SubCategory instance.
            ErrorResponse: A response containing validation errors if the data is invalid.
        """
        request_body = request.data
        request_body["location"] = str(location_id)
        request_body["department"] = str(department_id)
        request_body["category"] = str(category_id)
        serializer = SubCategorySerializer(data=request_body)
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return ErrorResponse(serializer.errors)

    def patch(self, request, subcategory_id):
        """
        Update an existing SubCategory instance partially.

        Args:
            request: The HTTP request object containing the update data.
            subcategory_id: The ID of the SubCategory instance to update.

        Returns:
            SuccessResponse: A response containing the updated SubCategory instance.
            ErrorResponse: A response containing validation errors if the data is invalid.
        """
        subcategory_instance = get_object_or_404(SubCategory, id=subcategory_id)
        serializer = SubCategorySerializer(
            instance=subcategory_instance, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(serializer.data)
        else:
            return ErrorResponse(serializer.errors)

    def delete(self, request, subcategory_id):
        """
        Delete a SubCategory instance.

        Args:
            request: The HTTP request object.
            subcategory_id: The ID of the SubCategory instance to delete.

        Returns:
            SuccessResponse: A response indicating successful deletion.
        """
        subcategory_instance = get_object_or_404(SubCategory, id=subcategory_id)
        subcategory_instance.delete()
        return SuccessResponse(status=status.HTTP_204_NO_CONTENT)


class StockKeepingUnitAPIView(APIView):
    """
    API view for handling requests related to StockKeepingUnit models.
    """

    def get(self, request):
        """
        Retrieve a list of StockKeepingUnit instances based on query parameters.

        Args:
            request: The HTTP request object containing query parameters for filtering.

        Returns:
            SuccessResponse: A response containing a list of filtered StockKeepingUnit instances.
            ErrorResponse: A response containing validation errors if the query parameters are invalid.
        """
        serialized_query_params = SKUQueryParamsSerializer(data=request.query_params)
        if not serialized_query_params.is_valid():
            return ErrorResponse(serialized_query_params.errors)

        skus = StockKeepingUnit.objects.filter(
            subcategory__name=request.GET.get("sub_category"),
            subcategory__category__name=request.GET.get("category"),
            subcategory__category__department__name=request.GET.get("department"),
            subcategory__category__department__location__name=request.GET.get(
                "location"
            ),
        )
        serializer = StockKeepingUnitSerializer(skus, many=True)
        return SuccessResponse(serializer.data)
