from django.contrib import admin

from random_id.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('article_name', 'order_id')


admin.site.register(Product, ProductAdmin)
