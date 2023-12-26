from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import *


def store(request):
    data = cartData(request)
    cart_items = data["cart_items"]
    products = Product.objects.all()
    context = {"products": products, "cart_items": cart_items}
    return render(request, "store/store.html", context)


def cart(request):
    data = cartData(request)
    items = data["items"]
    order = data["order"]
    cart_items = data["cart_items"]

    context = {"items": items, "order": order, "cart_items": cart_items}
    return render(request, "store/cart.html", context)


def checkout(request):
    data = cartData(request)
    items = data["items"]
    order = data["order"]
    cart_items = data["cart_items"]
    context = {"items": items, "order": order, "cart_items": cart_items}
    return render(request, "store/checkout.html", context)


def updateItem(request):
    data = json.loads(request.body)
    productid = data["productId"]
    action = data["action"]

    product = Product.objects.get(id=productid)
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        order_item.quantity += 1
    elif action == "remove":
        order_item.quantity -= 1
    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()
    return JsonResponse({"response": "Item was added!!!"})


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data["form"]["total"])
    order.transaction_id = transaction_id

    if total == float(order.get_order_total):
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data["shipping"]["address"],
            city=data["shipping"]["city"],
            state=data["shipping"]["state"],
            zipcode=data["shipping"]["zipcode"],
        )
    return JsonResponse({"response": "Transaction Completed"})
