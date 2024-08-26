from django.shortcuts import render, get_object_or_404
from .models import PRODUCTS, Category, TOPVBANNER
from .forms import FORMSEARCH


def get_shared_context():
    products = PRODUCTS.objects.all()
    categories = Category.objects.all()
    img = TOPVBANNER.objects.all()
    incrof = get_object_or_404(PRODUCTS, increadibleoffer=True)
    formsearch = FORMSEARCH()
    return {
        'products': products,
        'categories': categories,
        'img': img,
        'incrof': incrof,
        'formsearch': formsearch,
    }


def handle_search(request, products):
    if 'name' in request.GET:
        form = FORMSEARCH(request.GET)
        if form.is_valid():
            search = form.cleaned_data['name']
            return products.filter(name__icontains=search)
    return products


def product_view(request):
    context = get_shared_context()
    context['products'] = handle_search(request, context['products'])
    return render(request, 'product/center.html', context)


def product_detail(request, pk):
    context = get_shared_context()
    context['product'] = context['products'].filter(pk=pk)
    return render(request, 'product/details.html', context)


def product_cat(request, slug_cat):
    context = get_shared_context()
    category = get_object_or_404(Category, slug=slug_cat)
    context['products'] = handle_search(request, context['products'].filter(category=category))
    return render(request, 'product/categoryh.html', context)
