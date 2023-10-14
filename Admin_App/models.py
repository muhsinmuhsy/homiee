from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_image', null=True, blank=True)
    image_two = models.ImageField(upload_to='product_image', null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    actual_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.BooleanField(default=True)
    def __str__(self):
        return self.name
 

class SearchQuery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # default=1
    count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.product.name} - {self.count} searches"
    
class Activity(models.Model):
    text = models.CharField(max_length=250, null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
