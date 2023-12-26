import json
from .models import *


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES["cart"])
    except:
        cart = {}
    items = []
    order = {"get_order_total": 0, "get_order_item": 0, "shipping": False}
    cart_items = order["get_order_item"]

    for i in cart:
        try:
            cart_items += cart[i]["quantity"]

            product = Product.objects.get(id=i)
            total = product.price * cart[i]["quantity"]

            order["get_order_item"] += cart[i]["quantity"]
            order["get_order_total"] += total

            item = {
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "imageUrl": product.imageUrl,
                },
                "quantity": cart[i]["quantity"],
                "get_total": total,
            }
            items.append(item)

            if product.digital == False:
                order["shipping"] = True
        except:
            pass
    return {"items": items, "order": order, "cart_items": cart_items}


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_order_item
    else:
        cookieData = cookieCart(request)
        items = cookieData["items"]
        order = cookieData["order"]
        cart_items = cookieData["cart_items"]
    return {"items": items, "order": order, "cart_items": cart_items}


def guestOrder(request, data):
    print("COOKIES", request.COOKIES)

    name = data["form"]["name"]
    email = data["form"]["email"]

    cookieData = cookieCart(request)
    items = cookieData["items"]

    customer, created = Customer.objects.get_or_create(email=email)
    customer.name = name
    customer.save()

    order = Order.objects.create(customer=customer, complete=False)

    for item in items:
        product = Product.objects.get(id=item["product"]["id"])

        order_item = OrderItem.objects.create(
            product=product, order=order, quantity=item["quantity"]
        )
    return customer, order
