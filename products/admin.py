from django.contrib import admin

import products.models
from products.models import ProductCategory, Product



@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    fields = ('name', 'description',)
    ordering = ('name',)
    search_fields = ('name',)

    # @staticmethod
    # def category_id(cat_name):
    #     return ProductCategory.objects.filter(name=cat_name)
    #
    #
    # @staticmethod
    # def sum_prod_in_cat(self):
    #
    # def get_queryset(self, request):
    #     # print(Product.objects.filter(category=(super(ProductCategoryAdmin, self).get_queryset(request).filter())))
    #     # print(super(ProductCategoryAdmin, self).get_queryset(request).count())
    #     print(request)
    #     response = super(ProductCategoryAdmin, self).get_queryset(request)
    #     ips = list(set([obj.name for obj in response]))
    #     prod_qs = Product.objects.values('quantity', 'category')
    #     cat_qs = Product.objects.values('id', 'name')
    #
    #
    #     return response
    #
    # def quantity_of_products_in_category(self, instance):
    #     return self.quantity_of_products_in_category.get(instance.name)
    #
    # quantity_of_products_in_category.short_description = 'Количество товаров в категории'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category')
    readonly_fields = ('description',)
    ordering = ('-category',)
    search_fields = ('name',)
