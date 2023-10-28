from django.shortcuts import render
from .models import Order, OrderDetail, Cart, CartDetail

# Create your views here.


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/orders.html', {'orders' : orders})



def checkout(request):

    return render(request, 'orders/checkout.html' {

        
    })
