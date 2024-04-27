from django.shortcuts import render,get_object_or_404
from .models import*

# Create your views here.
def product (request):
    products=Product.objects.all()
    print(products)
    context={'products':products}
    return render (request,'Product.html',context)

def home (request):
    return render (request,'home.html')
   
def product_details(request,pk):
    products=get_object_or_404(Product,pk=pk)   
    context={'product':products} 
    return render (request,'product_details.html',context)