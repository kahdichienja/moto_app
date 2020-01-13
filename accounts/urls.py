from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_anme = 'accounts'
urlpatterns = [
    path('', views.homepage, name='home'),
    path('Oauth/', views.login_register, name = 'login_register'),
    path('reg/', views.user_register, name = 'user_register'),
    path('category/<int:id>', views.categorydetails, name = 'categorydetails'),
    path('product/<int:id>', views.productdetails, name = 'productdetails'),
    path('shop/', views.shop,  name = 'shop'),
    path('logout/', views.user_loguot, name = 'user_loguot'),
    path('cart/<int:id>/', views.add_to_shopping_cart, name = 'cart'),
    path('shopping/', views.shopping_cart, name = 'cartlist'),
    path('remove/<int:id>/', views.remove_cart, name = 'remove_cart'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('profile/', views.user_profile, name = 'user_profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)