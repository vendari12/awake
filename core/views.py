from django.shortcuts import render
from .models import item

# Create your views here.

def index(request):
    context = {
    'items': item.objects.all()
    }
    return render(request, "index.html", context)

def item_list(request):
    context  = {
        'items': item.objects.all()
    }
    return render(request, "cart.html", context)

def contact(request):
    return render(request, "contact.html")


def products(request):
    return render(request, "product.html")

def categories (request):
    return render(request, "categorie.html")

