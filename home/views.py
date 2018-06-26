from django.shortcuts import render
from .models import Service


def index(request):
    all_services = Service.objects.all()
    return render(request, 'home/index.html', {
        'all_services': all_services
    })
