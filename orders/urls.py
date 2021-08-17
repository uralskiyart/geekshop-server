from django.urls import path
from orders.views import OrderList

app_name = 'orders'


urlpatterns = [
    path('', OrderList.as_view(), name='orders_list'),
    path('order_create/<pk>/', OrderList.as_view(), name='order_read'),
    path('read/<pk>', OrderList.as_view(), name='order_read'),
    path('', OrderList.as_view(), name='order_update'),
    path('', OrderList.as_view(), name='order_delete'),
]