from django.shortcuts import render

def index(request):
    """Домашняя страница"""
    return render(request,"catalog/home.html")


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

