from django.contrib import admin

from sku.models import Category
from sku.models import Department
from sku.models import Location
from sku.models import StockKeepingUnit
from sku.models import SubCategory

# Register your models here.
admin.site.register([Location, Department, Category, SubCategory, StockKeepingUnit])
