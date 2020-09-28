from django.contrib import admin
from .models import *


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'email')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'item', 'quantity')


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
