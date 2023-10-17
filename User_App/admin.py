from django.contrib import admin
from User_App.models import *
# Register your models here.


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cart._meta.fields]

@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]

@admin.register(Review)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Review._meta.fields]


@admin.register(Enquiry)
class EnquiryModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Enquiry._meta.fields]

@admin.register(PlaceOrder)
class PlaceOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PlaceOrder._meta.fields]