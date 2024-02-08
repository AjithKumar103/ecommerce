from django.urls import path
from . import views

urlpatterns = [
    path("product-list/", views.productListApi, name="product-list"),
    path("add-to-cart/", views.addToCartApi, name="add-to-cart"),
]
