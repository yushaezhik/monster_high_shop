from django.shortcuts import render
from .data import DOLLS


def home(request):
    return render(request, 'index.html')


def doll_list(request):
    sort = request.GET.get('sort', 'name')

    if sort == 'price':
        dolls = sorted(DOLLS, key=lambda x: x['price'])
    elif sort == 'year':
        dolls = sorted(DOLLS, key=lambda x: x['year'])
    else:
        dolls = sorted(DOLLS, key=lambda x: x['name'].lower())

    return render(request, 'dolls/list.html', {'dolls': dolls, 'sort': sort})


def doll_detail(request, slug):
    doll = next((item for item in DOLLS if item['slug'] == slug), None)
    return render(request, 'dolls/detail.html', {'doll': doll})