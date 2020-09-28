from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return f"{self.name} : {self.price}"


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return f"{self.user.username}"

# better name = Order
class OrderItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.customer.user.username} : {self.item} - {self.quantity}"
