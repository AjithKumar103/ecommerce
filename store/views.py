from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_order_item
    else:
        items = []
        order = {"get_order_total": 0, "get_order_item": 0}
        cart_items = order["get_order_item"]
    products = Product.objects.all()
    context = {"products": products, "cart_items": cart_items}
    return render(request, "store/store.html", context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_order_item
    else:
        items = []
        order = {"get_order_total": 0, "get_order_item": 0}
        cart_items = order["get_order_item"]
    context = {"items": items, "order": order, "cart_items": cart_items}
    return render(request, "store/cart.html", context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_order_item
    else:
        items = []
        order = {"get_order_total": 0, "get_order_item": 0}
        cart_items = order["get_order_item"]
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
        else:
            print("User is Logged In")

    return JsonResponse({"response": "Transaction Completed"})
