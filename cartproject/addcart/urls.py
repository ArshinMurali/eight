from . import views
from django.urls import path
app_name = 'addcart'
urlpatterns = [
    path('add/<int:product_id>/', views.adding_cart, name='adding_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('full_delete/<int:product_id>/', views.full_delete, name='full_delete'),
]
