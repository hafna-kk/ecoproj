
from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

def SearchResult(request):
    query = request.GET.get('q')
    products = Product.objects.all()

    if query:
        products = products.filter(Q(name__contains=query) | Q(description__contains=query))

    return render(request, "search.html", {'query': query, 'products': products})
