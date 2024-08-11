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
    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return SuccessResponse(serializer.data)

    def post(self, request):
        request_body = request.data
        serializer = LocationSerializer(data=request_body)
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return ErrorResponse(serializer.errors)

    def patch(self, request, location_id):
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
        location_instance = get_object_or_404(Location, id=location_id)
        location_instance.delete()
        return SuccessResponse(status=status.HTTP_204_NO_CONTENT)


class DepartmentsAPIView(APIView):
    def get(self, request, location_id):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return SuccessResponse(serializer.data)

    def post(self, request, location_id):
        request_body = request.data
        request_body["location"] = str(location_id)
        serializer = DepartmentSerializer(data=request_body)
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return ErrorResponse(serializer.errors)

    def patch(self, request, department_id):
        location_instance = get_object_or_404(Department, id=department_id)
        serializer = DepartmentSerializer(
            instance=location_instance, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(serializer.data)
        else:
            return ErrorResponse(serializer.errors)

    def delete(self, request, department_id):
        location_instance = get_object_or_404(Department, id=department_id)
        location_instance.delete()
        return SuccessResponse(status=status.HTTP_204_NO_CONTENT)


class CategoriesAPIView(APIView):
    def get(self, request, location_id, department_id):
        departments = Category.objects.all()
        serializer = CategorySerializer(departments, many=True)
        return SuccessResponse(serializer.data)

    def post(self, request, location_id, department_id):
        request_body = request.data
        request_body["location"] = str(location_id)
        request_body["department"] = str(department_id)
        serializer = CategorySerializer(data=request_body)
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return ErrorResponse(serializer.errors)

    def patch(self, request, category_id):
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
        subcategory_instance = get_object_or_404(Category, id=category_id)
        subcategory_instance.delete()
        return SuccessResponse(status=status.HTTP_204_NO_CONTENT)


class SubCategoriesAPIView(APIView):
    def get(self, request, location_id, department_id, category_id):
        departments = SubCategory.objects.all()
        serializer = SubCategorySerializer(departments, many=True)
        return SuccessResponse(serializer.data)

    def post(self, request, location_id, department_id, category_id):
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
        subcategory_instance = get_object_or_404(SubCategory, id=subcategory_id)
        subcategory_instance.delete()
        return SuccessResponse(status=status.HTTP_204_NO_CONTENT)


class StockKeepingUnitAPIView(APIView):
    def get(self, request):
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
