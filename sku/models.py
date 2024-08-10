from django.db import models

from base.models import BaseModel


class Location(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Department(BaseModel):
    location = models.ForeignKey(
        Location, related_name="departments", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(BaseModel):
    department = models.ForeignKey(
        Department, related_name="categories", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(BaseModel):
    category = models.ForeignKey(
        Category, related_name="subcategories", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class StockKeepingUnit(BaseModel):
    subcategory = models.ForeignKey(
        SubCategory, related_name="skus", on_delete=models.CASCADE
    )
    sku_code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.sku_code} - {self.name}"
