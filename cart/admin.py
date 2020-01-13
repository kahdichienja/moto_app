from django.contrib import admin
from cart.models import Cart, Order
# Register your models here.


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["id","user","product","total", "qnty", "updated", "timestamp"]
    list_display_links = ["user"]
    list_filter = ["user"]
    search_fields = ["user", "timestamp"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id","user"]
    list_display_links = ["user"]
    list_filter = ["user"]
    search_fields = ["user"]
