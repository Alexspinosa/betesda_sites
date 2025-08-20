
from django.shortcuts import render, get_object_or_404
from .models import Menu

def home(request):
    menu = get_object_or_404(Menu, slug='main')  # Aquí usas el slug de tu menú
    return render(request, 'home/home.html', {
        'menu': menu,
    })
