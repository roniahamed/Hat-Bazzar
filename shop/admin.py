from django.contrib import admin
from .models import Products, Order

admin.site.register(Order)
admin.site.register(Products)