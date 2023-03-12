from django.shortcuts import render, get_object_or_404

from .models import Product, Category
#Category ni o'chirdim

def frontpage(request):
    products = Product.objects.all()

    context = {
        'products' : products,
    }


    return render(request, 'frontpage.html', context)

def single(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product' : product,
    }


    return render(request, 'single.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()

    context = {
        'category' : category,
        'products' : products,

    }


    return render(request, 'category_detail.html', context)     