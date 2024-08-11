from ast import Mod
from dataclasses import field
from pydoc import locate

from rest_framework import serializers

from sku.models import Category
from sku.models import Department
from sku.models import Location
from sku.models import StockKeepingUnit
from sku.models import SubCategory


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"


class StockKeepingUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockKeepingUnit
        fields = "__all__"


class SKUQueryParamsSerializer(serializers.Serializer):
    location = serializers.CharField(required=True, max_length=100)
    department = serializers.CharField(required=True, max_length=100)
    category = serializers.CharField(required=True, max_length=100)
    sub_category = serializers.CharField(required=True, max_length=100)
