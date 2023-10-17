from django.db import models
from U_Auth.models import User
from Admin_App.models import Product 
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # price always change thats why this using
    price_dummy = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    quantity = models.IntegerField(default=1)

    # the total of the one cart price_dummy*quantity
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # for ordered cart not selecting in order
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.price_dummy)



# automatically saving price dummy from productvariant price 
@receiver(pre_save, sender=Cart)
def auto_save_price_dummy(sender, instance, **kwargs):
    product = instance.product
    # if there is discount price saving siscount price else saving actual price
    if product:
        if product.discount_price:
            instance.price_dummy = product.discount_price
        else:
            instance.price_dummy = product.actual_price

# atomatically calculating the price_dummy*quantity
@receiver(pre_save, sender=Cart)
def auto_cart_total(sender, instance, **kwargs):
    instance.total = instance.price_dummy * instance.quantity   


class PlaceOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postel_code = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    order_note = models.CharField(max_length=250, null=True, blank=True)


class Order(models.Model):
    STATUS = (
        ('PENDING', 'PENDING'),
        ('ORDER CORNFIMED', 'ORDER CORNFIMED'),
        ('SHIPPED', 'SHIPPED'),
        ('ORDER DONE', 'ORDER DONE'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ManyToManyField(Cart)
    place_order = models.ForeignKey(PlaceOrder, on_delete=models.CASCADE, default=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    shipping_charge = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_of_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS, default='PENDING')
    delivery_espected = models.CharField(max_length=100, null=True, blank=True)
    paid= models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    head = models.CharField(max_length=25)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=500)