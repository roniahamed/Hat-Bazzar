from django.shortcuts import render
from .models import Products, Order 
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

def checkout(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        address = request.POST.get('address','')
        city = request.POST.get('city','')
        zipcode = request.POST.get('zip_code','')
    order = Order(name=name,email=email, phone=phone,address=address, city=city, zipcode=zipcode)
    
    return render(request, 'shop/checkout.html')