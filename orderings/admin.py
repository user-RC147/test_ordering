from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Client, Product, OrderItem


# Налаштування для товарів
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    search_fields = ['name']




@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    search_fields = ['name']