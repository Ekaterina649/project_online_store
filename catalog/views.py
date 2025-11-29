from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def index(request):
    """Домашняя страница"""
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'catalog/home.html', context)


def contacts(request):
    """Страница контактов"""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f"Новое сообщение от: {name}, телефон: {phone}, сообщение: {message}")


        return render(request, 'catalog/contacts.html', {
            'success': True,
            'name': name,
            'phone': phone,
            'message': message
        })

    return render(request, 'catalog/contacts.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'catalog/product_detail.html',context)
