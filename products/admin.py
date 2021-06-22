from django.contrib import admin

from products.models import ProductCategory, Product



@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','quantity_in_category')
    fields = ('name', 'description','quantity_in_category')
    ordering = ('name',)
    search_fields = ('name',)


    def quantity_in_category(self, obj):
        return sum(product.quantity for product in Product.objects.filter(category=obj.name))



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category')
    readonly_fields = ('description',)
    ordering = ('-category',)
    search_fields = ('name',)
