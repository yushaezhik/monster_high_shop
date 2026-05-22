from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from dolls import views as dolls_views
from cart import views as cart_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dolls_views.home, name='home'),
    path('dolls/', dolls_views.doll_list, name='doll_list'),
    path('dolls/<slug:slug>/', dolls_views.doll_detail, name='doll_detail'),

    path('cart/', cart_views.cart_view, name='cart'),
    path('cart/add/<slug:slug>/', cart_views.add_to_cart, name='add_to_cart'),
    path('cart/checkout/', cart_views.checkout, name='checkout'),

    path('login/', cart_views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', cart_views.register_view, name='register'),
    path('cart/increase/<slug:slug>/', cart_views.increase_cart, name='increase_cart'),
    path('cart/decrease/<slug:slug>/', cart_views.decrease_cart, name='decrease_cart'),
]