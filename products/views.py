from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'products/product_form.html'
    fields = ['title', 'description', 'base_price', 'color_white_price', 'color_black_price', 'color_red_price', 'image']

