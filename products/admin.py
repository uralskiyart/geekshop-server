from django.contrib import admin

import products.models
from products.models import ProductCategory, Product



@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'quantity_of_products_in_category')
    fields = ('name', 'description',)
    ordering = ('name',)
    search_fields = ('name',)

    @staticmethod
    def category_id(cat_name):
        return ProductCategory.objects.filter(name=cat_name)


    @staticmethod
    def sum_prod_in_cat(self):
        pass


    def quantity_of_products_in_category(self, instance):
        print(Product.objects.filter(category=instance.id))
        return Product.objects.filter(category=instance.id).count()

    quantity_of_products_in_category.short_description = ('Количество моделей в категории')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category')
    readonly_fields = ('description',)
    ordering = ('-category',)
    search_fields = ('name',)
