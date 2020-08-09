from django.shortcuts import render, get_object_or_404
from products.models import Product
from django.contrib.auth.decorators import login_required


@login_required
def product_detail(request, pk):
    # product = get_object_or_404(Product, pk=pk)
    # product = Product.objects.get(id=pk)
    product = Product.objects.all()[0]
    return render(request, 'product_detail.html', {'product': product})
