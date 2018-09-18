from django.shortcuts import render

# Create your views here.
def index(request):
     return render(request, 'index.html')
 
def orders(request):
    return render(request, 'orders.html')

def customers(request):
    return render(request, 'customers.html')