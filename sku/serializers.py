from ast import Mod
from dataclasses import field

from rest_framework.serializers import ModelSerializer

from sku.models import Category
from sku.models import Department
from sku.models import Location
from sku.models import StockKeepingUnit
from sku.models import SubCategory


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"


class StockKeepingUnitSerializer(ModelSerializer):
    class Meta:
        model = StockKeepingUnit
        fields = "__all__"
