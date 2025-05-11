from django.shortcuts import render
from .models import Products 
from django.core.paginator import Paginator


def index(request):
    product_objects = Products.objects.only('id')
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = Products.objects.filter(title__icontains=item_name)
    paginator = Paginator(product_objects, 100)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_objects':product_objects})


def single_product(request, id):
    product_object = Products.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_object':product_object})