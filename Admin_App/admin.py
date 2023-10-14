from django.contrib import admin
from Admin_App.models import *

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]


@admin.register(SearchQuery)
class SearchQueryModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SearchQuery._meta.fields]

@admin.register(Activity)
class ActivityModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Activity._meta.fields]