from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import get_object_or_404

def home(request):
    from .models import Product
    popular_products = Product.objects.order_by('-created_at')[:3]  # покажем последние 3 товара
    return render(request, 'catalog/home.html', {'popular_products': popular_products})


def catalog(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_id:
        products = products.filter(category_id=category_id)
    return render(request, 'catalog/catalog.html', {
        'products': products,
        'categories': categories,
        'selected_category': category_id
    })

def about(request):
    return render(request, 'catalog/about.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    
    return render(request, 'catalog/product_detail.html', {
        'product': product,
        'related_products': related_products
    })
