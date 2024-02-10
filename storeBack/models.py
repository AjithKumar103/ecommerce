from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.IntegerField()
    type = models.CharField(
        max_length=3,
        choices=[
            ("rc", "cereal"),
            ("cs", "spices"),
            ("sb", "snacks"),
        ],
    )
    image = models.ImageField(upload_to="product_pics", null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True
    )
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return str(self.id)

    @property
    def get_total_order_cost(self):
        items = self.order_items.all()
        return sum([item.get_total for item in items])

    @property
    def get_total_order_items(self):
        items = self.order_items.all()
        return sum([item.quantity for item in items])

    # @property
    # def shipping(self):
    #     shipping = False
    #     items = self.orderitem_set.all()
    #     for i in items:
    #         if i.product.digital == False:
    #             shipping = True
    #     return shipping


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True
    )
    order = models.ForeignKey(
        Order,
        related_name="order_items",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    quantity = models.IntegerField(default=0, null=True, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        return self.product.price * self.quantity


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True
    )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    pincode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.address
