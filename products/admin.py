from django.contrib import admin

from products.models import ProductCategory, Product


# admin.site.register(ProductCategory)
# @admin.register(ProductCategory)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description',)
#     fields = ('name', 'description',)
#     ordering = ('name',)
#     search_fields = ('name',)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category')
    readonly_fields = ('description',)
    ordering = ('-category',)
    search_fields = ('name',)
