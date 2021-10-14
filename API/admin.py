from django.contrib import admin

from API.models import productos
from .models import productos


class ProductosAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'price', 'description', 'created', 'updated'
    )

admin.site.register(productos, ProductosAdmin)
