from django.contrib import admin

from products.models import ProductCategory, Product



@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    fields = ('name', 'description',)
    ordering = ('name',)
    search_fields = ('name',)


    def get_queryset(self, request):
        print(ProductCategory.products_in_category_sum)
        print(super(ProductCategoryAdmin, self).get_queryset(request).count())
        return super(ProductCategoryAdmin, self).get_queryset(request)

    def quantity_of_products_in_category(self, obj):
        return obj.quantity_of_products_in_category
    quantity_of_products_in_category.short_description = f'Количество товаров в категории '


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category')
    readonly_fields = ('description',)
    ordering = ('-category',)
    search_fields = ('name',)
