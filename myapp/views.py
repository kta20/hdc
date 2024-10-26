from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def home(request):
    return render (request, 'myapp/home.html')

def products(request):
    return render(request, 'myapp/products.html')

