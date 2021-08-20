from django.urls import path
from orders.views import OrderList, OrderItemCreate, OrderItemUpdate, OrderItemDelete, OrderItemRead, \
    order_forming_complete

app_name = 'orders'


urlpatterns = [
    path('', OrderList.as_view(), name='order_list'),
    path('create/', OrderItemCreate.as_view(), name='order_create'),
    path('read/<pk>/', OrderItemRead.as_view(), name='order_read'),
    path('update/<pk>/', OrderItemUpdate.as_view(), name='order_update'),
    path('delete/<pk>/', OrderItemDelete.as_view(), name='order_delete'),
    path('forming/complete/<pk>/', order_forming_complete, name='order_forming_complete')
]