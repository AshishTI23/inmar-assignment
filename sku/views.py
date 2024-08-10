from rest_framework.views import APIView

from base.http import ErrorResponse
from base.http import SuccessResponse
from sku import serializers
from sku.models import Category
from sku.models import Department
from sku.models import Location
from sku.models import StockKeepingUnit
from sku.models import SubCategory
from sku.serializers import CategorySerializer
from sku.serializers import DepartmentSerializer
from sku.serializers import LocationSerializer
from sku.serializers import StockKeepingUnitSerializer
from sku.serializers import SubCategorySerializer


class LocationsAPIView(APIView):
    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return SuccessResponse(serializer.data)


class DepartmentsAPIView(APIView):
    def get(self, request, location_id):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        print(serializer.data)
        return SuccessResponse(serializer.data)


class CategoriesAPIView(APIView):
    def get(self, request, location_id, department_id):
        departments = Category.objects.all()
        serializer = CategorySerializer(departments, many=True)
        print(serializer.data)
        return SuccessResponse(serializer.data)


class SubCategoriesAPIView(APIView):
    def get(self, request, location_id, department_id, category_id):
        departments = SubCategory.objects.all()
        serializer = SubCategorySerializer(departments, many=True)
        print(serializer.data)
        return SuccessResponse(serializer.data)


class StockKeepingUnitAPIView(APIView):
    def get(self, request):
        departments = StockKeepingUnit.objects.all()
        serializer = StockKeepingUnitSerializer(departments, many=True)
        print(serializer.data)
        return SuccessResponse(serializer.data)
