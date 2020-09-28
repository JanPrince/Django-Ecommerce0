from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="products"),
    path('cart/', views.cart, name='cart'),
]