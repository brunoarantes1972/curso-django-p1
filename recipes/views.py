from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Obi Wan Kenobi',
    })


def about(request):
    return HttpResponse('about')
