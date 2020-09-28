from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    context = {
        'products': Product.objects.all()
    }
    print(request.user)
    return render(request, 'products/home.html', context)


def cart(request):
    context = {}
    return render(request, 'products/cart.html', context)
