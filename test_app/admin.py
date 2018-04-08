from django.contrib import admin

from test_app.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('article_name', 'order_id')


admin.site.register(Product, ProductAdmin)



# Register your models here.
