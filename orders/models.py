from django.db import models

from geekshop import settings
from products.models import Product


class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    DELIVERY = 'DLV'
    DONE = 'DN'
    CANCELED = 'CNC'

    STATUSES = (
        (FORMING, 'формирование'),
        (SENT_TO_PROCEED, 'передан в обработку'),
        (DELIVERY, 'доставка'),
        (DONE, 'выдан'),
        (CANCELED, 'отменен'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUSES, default=FORMING, max_length=3)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ('-created_at', )

    def __str__(self):
        return f'Заказ номер {self.pk}'

    def get_total_quantity(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, items)))

    def get_total_cost(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.get_product_cost, items)))

    def delete(self):
        self.is_active = False
        self.save()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    @property
    def get_product_cost(self):
        return self.quantity * self.product.price
