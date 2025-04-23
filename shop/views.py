from django.shortcuts import render
from .models import Products 


def index(request):
    product_objects = Products.objects.all()
    return render(request, 'shop/index.html', {'product_objects':product_objects})
