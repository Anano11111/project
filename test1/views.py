from django.shortcuts import render
from .models import Product
# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request,'home.html', {'productS':products})



def product_detail(request):
    return render(request,'product_detail.html')