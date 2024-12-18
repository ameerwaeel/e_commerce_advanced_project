from django.contrib import admin

# Register your models here.
from . models import *

admin.site.register(Category)
admin.site.register(Product)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     readonly_fields=['slug']


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     readonly_fields=['slug']    
# from django.contrib import admin
# from .models import Product, Category

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     readonly_fields = ['slug']
#     list_display = ['name', 'price', 'status', 'created_at']
#     list_filter = ['status', 'created_at']
#     search_fields = ['name', 'description']
#     prepopulated_fields = {"slug": ("name",)}  # يجعل الحقل slug يتم ملؤه تلقائيًا من name

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     readonly_fields = ['slug']
#     list_display = ['name', 'created']
#     search_fields = ['name']
#     prepopulated_fields = {"slug": ("name",)}  # يجعل الحقل slug يتم ملؤه تلقائيًا من name
