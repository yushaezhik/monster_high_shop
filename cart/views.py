from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.decorators.http import require_POST

from .forms import RegisterForm, LoginForm
from dolls.data import DOLLS as DOLL_LIST

DOLLS = {item['slug']: item for item in DOLL_LIST}


@login_required
def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for slug, qty in cart.items():
        doll = DOLLS.get(slug)
        if doll:
            item_total = doll['price'] * qty
            total += item_total
            items.append({
                'slug': slug,
                'name': doll['name'],
                'price': doll['price'],
                'quantity': qty,
                'total': item_total,
                'image': doll['image'],
            })

    return render(request, 'cart/cart.html', {'items': items, 'total': total})


@login_required
@require_POST
def add_to_cart(request, slug):
    cart = request.session.get('cart', {})
    cart[slug] = cart.get(slug, 0) + 1
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart')


@login_required
@require_POST
def increase_cart(request, slug):
    cart = request.session.get('cart', {})
    cart[slug] = cart.get(slug, 0) + 1
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart')


@login_required
@require_POST
def decrease_cart(request, slug):
    cart = request.session.get('cart', {})
    if slug in cart:
        if cart[slug] > 1:
            cart[slug] -= 1
        else:
            del cart[slug]
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart')


@login_required
@require_POST
def checkout(request):
    request.session['cart'] = {}
    request.session.modified = True
    return render(request, 'cart/checkout_done.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cart')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    form = LoginForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        return redirect('cart')
    return render(request, 'registration/login.html', {'form': form})