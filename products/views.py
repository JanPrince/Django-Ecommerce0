from django.http import JsonResponse
from django.shortcuts import render
from .models import *
import json


# Create your views here.
def index(request):
    print(request.user)
    cart_num = len(request.user.customer.orders.all())
    context = {
        'products': Product.objects.all(),
        "cart": cart_num,
    }
    print(request.user)
    return render(request, 'products/home.html', context)


def cart(request):
    context = {}
    return render(request, 'products/cart.html', context)


def updateCart(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print(f"ProductId: {productId}")
    print(f"Action: {action}")

    customer = request.user.customer
    product = Product.objects.get(id=productId)

    try:
        order = OrderItem.objects.get(customer=customer, item=product)
        if action == 'add':
            order.quantity = order.quantity + 1
            order.save()

    except OrderItem.DoesNotExist:
        order = OrderItem(customer=customer, item=product, quantity=1)
        order.save()

    # The code below does not work- since i would be trying to get only the OrderItem with quantity=1
    # order, created = OrderItem.objects.get_or_create(customer=customer, item=product, quantity=1)
    #
    # if created == False and action == 'add':
    #     order.quantity = (order.quantity + 1)
    #     print(order.quantity)
    #
    # order.save()
    cart_ = len(customer.orders.all())
    return JsonResponse({
        'message': 'Item was added',
        'cart' : cart_
    })
