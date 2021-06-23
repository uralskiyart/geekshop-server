from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    # @property
    # def products_in_category(self):
    #     return Product.objects.filter(category=self.name)
    #
    # def products_in_category_sum(self):
    #     return sum(product.quantity for product in self.products_in_category)


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=256)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField(verbose_name='описание продукта', max_length=64, blank=True, null=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    def __str__(self):
        return f"{self.name} ({self.category.name})"


