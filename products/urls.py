from django.urls import path

from products.views import products

app_name = 'products'

urlpatterns = [
    path('<int:category_id>/', products, name='product'),
    path('', products, name='index'),
]