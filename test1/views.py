from django.shortcuts import render
from .models import Product
# Create your views here.

def home(request):
    products = Product.objects.all()
    print(request.GET)
    filters= dict()

    product_name = request.GET.get('product_name')
    if product_name:
        products = products.filter(name__icontains = product_name)
    min_price = request.GET.get('min_price')
    if  min_price:
        products = products.filter(price__gt=min_price)

    max_price = request.GET.get('max_price')
    if  max_price:
        products = products.filter(price__gt=max_price)

    address = request.GET.get('address')
    if  address:
        filters['address__icontains'] = address

    category = request.GET.get('category')
    if  category:
        filters['category__id'] = category

    products = products.objects.filter(**filters)
    categories = Category.object.all()


    return render(request,'home.html', {'productS':products})



def product_detail(request):
    return render(request,'product_detail.html')