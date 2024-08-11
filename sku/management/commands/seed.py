from django.core.management.base import BaseCommand
from django.db import transaction

from sku.models import Category
from sku.models import Department
from sku.models import Location
from sku.models import StockKeepingUnit
from sku.models import SubCategory

META_DATA_SEED = [
    ["Perimeter", "Bakery", "Bakery Bread", "Bagels"],
    ["Perimeter", "Bakery", "Bakery Bread", "Baking or Breading Products"],
    ["Perimeter", "Bakery", "Bakery Bread", "English Muffins or Biscuits"],
    ["Perimeter", "Bakery", "Bakery Bread", "Flatbreads"],
    ["Perimeter", "Bakery", "In Store Bakery", "Breakfast Cake or Sweet Roll"],
    ["Perimeter", "Bakery", "In Store Bakery", "Cakes"],
    ["Perimeter", "Bakery", "In Store Bakery", "Pies"],
    ["Perimeter", "Bakery", "In Store Bakery", "Seasonal"],
    ["Center", "Dairy", "Cheese", "Cheese Sauce"],
    ["Center", "Dairy", "Cheese", "Specialty Cheese"],
    ["Center", "Dairy", "Cream or Creamer", "Dairy Alternative Creamer"],
    ["Center", "Dairy", "Cream or Creamer", "Whipping Creams"],
    ["Center", "Dairy", "Cultured", "Cottage Cheese"],
    ["Center", "Dairy", "Refrigerated Baking", "Refrigerated Breads"],
    [
        "Center",
        "Dairy",
        "Refrigerated Baking",
        "Refrigerated English Muffins and Biscuits",
    ],
    ["Center", "Dairy", "Refrigerated Baking", "Refrigerated Hand Held Sweets"],
    ["Center", "Dairy", "Refrigerated Baking", "Refrigerated Pie Crust"],
    [
        "Center",
        "Dairy",
        "Refrigerated Baking",
        "Refrigerated Sweet Breakfast Baked Goods",
    ],
    ["Perimeter", "Deli and Foodservice", "Self Service Deli Cold", "Beverages"],
    ["Perimeter", "Deli and Foodservice", "Service Deli", "Cheese All Other"],
    ["Perimeter", "Deli and Foodservice", "Service Deli", "Cheese American"],
    ["Perimeter", "Floral", "Bouquets and Cut Flowers", "Bouquets and Cut Flowers"],
    ["Perimeter", "Floral", "Gifts", "Gifts"],
    ["Perimeter", "Floral", "Plants", "Plants"],
    ["Center", "Frozen", "Frozen Bake", "Bread or Dough Products Frozen"],
    ["Center", "Frozen", "Frozen Bake", "Breakfast Cake or Sweet Roll Frozen"],
    ["Center", "Frozen", "Frozen Breakfast", "Frozen Breakfast Entrees"],
    ["Center", "Frozen", "Frozen Breakfast", "Frozen Breakfast Sandwich"],
    ["Center", "Frozen", "Frozen Breakfast", "Frozen Egg Substitutes"],
    ["Center", "Frozen", "Frozen Breakfast", "Frozen Syrup Carriers"],
    ["Center", "Frozen", "Frozen Desserts or Fruit and Toppings", "Pies Frozen"],
    ["Center", "Frozen", "Frozen Juice", "Frozen Apple Juice"],
    ["Center", "Frozen", "Frozen Juice", "Frozen Fruit Drink Mixers"],
    ["Center", "Frozen", "Frozen Juice", "Frozen Fruit Juice All Other"],
    ["Center", "GM", "Audio Video", "Audio"],
    ["Center", "GM", "Audio Video", "Video DVD"],
    ["Center", "GM", "Audio Video", "Video VHS"],
    ["Center", "GM", "Housewares", "Bedding"],
    ["Center", "GM", "Housewares", "Candles"],
    ["Center", "GM", "Housewares", "Collectibles and Gifts"],
    ["Center", "GM", "Housewares", "Flashlights"],
    ["Center", "GM", "Housewares", "Frames"],
    ["Center", "GM", "Insect and Rodent", "Indoor Repellants or Traps"],
    ["Center", "GM", "Insect and Rodent", "Outdoor Repellants or Traps"],
    ["Center", "GM", "Kitchen Accessories", "Kitchen Accessories"],
    ["Center", "GM", "Laundry", "Bleach Liquid"],
    ["Center", "GM", "Laundry", "Bleach Powder"],
    ["Center", "GM", "Laundry", "Fabric Softener Liquid"],
    ["Center", "GM", "Laundry", "Fabric Softener Sheets"],
    ["Center", "Grocery", "Baking Ingredients", "Dry or Canned Milk"],
    ["Center", "Grocery", "Baking Ingredients", "Food Coloring"],
    ["Center", "Grocery", "Spices", "Salt Cooking or Edible or Seasoned"],
    ["Center", "Grocery", "Spices", "Salt Substitute"],
    ["Center", "Grocery", "Spices", "Seasoning Dry"],
    ["Center", "Grocery", "Stuffing Products", "Stuffing Products"],
    ["Perimeter", "Seafood", "Frozen Shellfish", "Frozen Shellfish"],
    ["Perimeter", "Seafood", "Other Seafood", "All Other Seafood"],
    ["Perimeter", "Seafood", "Other Seafood", "Prepared Seafood Entrees"],
    ["Perimeter", "Seafood", "Other Seafood", "Seafood Salads"],
    ["Perimeter", "Seafood", "Other Seafood", "Smoked Fish"],
    ["Perimeter", "Seafood", "Other Seafood", "Seafood Breading Sauces Dips"],
]

SKU_DATA_SEED = [
    ["1", "SKUDESC1", "Perimeter", "Bakery", "Bakery Bread", "Bagels"],
    [
        "2",
        "SKUDESC2",
        "Perimeter",
        "Deli and Foodservice",
        "Self Service Deli Cold",
        "Beverages",
    ],
    [
        "3",
        "SKUDESC3",
        "Perimeter",
        "Floral",
        "Bouquets and Cut Flowers",
        "Bouquets and Cut Flowers",
    ],
    ["4", "SKUDESC4", "Perimeter", "Deli and Foodservice", "Service Deli", "All Other"],
    [
        "5",
        "SKUDESC5",
        "Center",
        "Frozen",
        "Frozen Bake",
        "Bread or Dough Products Frozen",
    ],
    ["6", "SKUDESC6", "Center", "Grocery", "Crackers", "Rice Cakes"],
    ["7", "SKUDESC7", "Center", "GM", "Audio Video", "Audio"],
    ["8", "SKUDESC8", "Center", "GM", "Audio Video", "Video DVD"],
    ["9", "SKUDESC9", "Perimeter", "GM", "Housewares", "Bedding"],
    ["10", "SKUDESC10", "Perimeter", "Seafood", "Frozen Shellfish", "Frozen Shellfish"],
    ["11", "SKUDESC11", "Perimeter", "Seafood", "Other Seafood", "All Other Seafood"],
    [
        "12",
        "SKUDESC12",
        "Perimeter",
        "Seafood",
        "Other Seafood",
        "Prepared Seafood Entrees",
    ],
    ["13", "SKUDESC13", "Perimeter", "Seafood", "Other Seafood", "Seafood Salads"],
    ["14", "SKUDESC14", "Perimeter", "Bakery", "Bakery Bread", "Bagels"],
    [
        "15",
        "SKUDESC15",
        "Perimeter",
        "Deli and Foodservice",
        "Self Service Deli Cold",
        "Beverages",
    ],
    [
        "16",
        "SKUDESC16",
        "Perimeter",
        "Floral",
        "Bouquets and Cut Flowers",
        "Bouquets and Cut Flowers",
    ],
    [
        "17",
        "SKUDESC17",
        "Perimeter",
        "Deli and Foodservice",
        "Service Deli",
        "All Other",
    ],
    [
        "18",
        "SKUDESC18",
        "Center",
        "Frozen",
        "Frozen Bake",
        "Bread or Dough Products Frozen",
    ],
]


class Command(BaseCommand):
    help = (
        "Create metadata and stock keeping units from seed data with optional arguments"
    )

    def add_arguments(self, parser):
        # Optional argument to specify a seed type to process
        parser.add_argument(
            "--type",
            type=str,
            help="Metadata will be seeded",
        )

    def handle(self, *args, **options):
        type = options.get("type")

        if type == "add":
            self.create_metadata_records()
            self.create_stock_keeping_units()
        elif type == "delete":
            self.delete_metadata_records()
            self.delete_stock_keeping_units()

    @transaction.atomic
    def create_metadata_records(self):
        for row in META_DATA_SEED:
            location, _ = Location.objects.get_or_create(name=row[0])

            department, _ = Department.objects.get_or_create(
                name=row[1], location=location
            )

            category, _ = Category.objects.get_or_create(
                name=row[2], department=department
            )

            SubCategory.objects.get_or_create(name=row[3], category=category)

    @transaction.atomic
    def create_stock_keeping_units(self):
        for sku_row in SKU_DATA_SEED:
            (
                code,
                sku_name,
                location_name,
                department_name,
                category_name,
                subcategory_name,
            ) = sku_row

            location, _ = Location.objects.get_or_create(name=location_name)
            department, _ = Department.objects.get_or_create(
                name=department_name, location=location
            )
            category, _ = Category.objects.get_or_create(
                name=category_name, department=department
            )
            subcategory, _ = SubCategory.objects.get_or_create(
                name=subcategory_name, category=category
            )

            StockKeepingUnit.objects.get_or_create(
                sku_code=code, name=sku_name, subcategory=subcategory
            )

    @transaction.atomic
    def delete_metadata_records(self):
        Location.objects.all().delete()
        Department.objects.all().delete()
        Category.objects.all().delete()
        SubCategory.objects.all().delete()

    @transaction.atomic
    def delete_stock_keeping_units(self):
        StockKeepingUnit.objects.all().delete()
