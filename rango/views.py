from django.http import HttpResponse
from django.shortcuts import render

from rango.models import Category, Page


def index(request):
    categories_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': categories_list}

    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html')
