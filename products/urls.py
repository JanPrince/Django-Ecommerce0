from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="products"),
    path('cart/', views.cart, name='cart'),
    path('update_cart/', views.updateCart, name='update')
]