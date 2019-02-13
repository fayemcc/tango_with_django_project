from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from rango.models import Category, Page


def index(request):
    categories_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': categories_list}

    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html')


def show_category(request, category_name_slug):

    context_dict = {}

    try:
        category = Category.objects.get(slug=(category_name_slug[:-1]))

        pages = Page.objects.filter(category=category)

        context_dict['category'] = category
        context_dict['pages'] = pages

    except ObjectDoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)
