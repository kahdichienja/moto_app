from django.contrib import admin
from product.models import Category, Product, ProductAttribute
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","category_name"]
    list_display_links = ["category_name"]
    list_filter = ["category_name"]
    search_fields = ["category_name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["category","product_name","product_price","number_in_stock"]
    list_display_links = ["product_name"]
    list_filter = ["product_name"]
    search_fields = ["product_name"]

@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ["id","product"]
    list_display_links = ["product"]
    list_filter = ["product"]
    search_fields = ["product"]
    

