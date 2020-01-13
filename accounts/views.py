from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from product.models import Product, Category, ProductAttribute
from django.core.exceptions import ObjectDoesNotExist
from accounts.forms import UserLoginForm, UserRegisterForm
from cart.models import Cart, Order

# Create your views here.
def login_register(request):
    all_category_qs = Category.objects.all()
    if request.user.is_authenticated:
        messages.success(request, f'login was Success! { request.user.username }')
        return redirect('/')#change to profile
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            login(request, user)

            messages.success(request, f'login was Success {username} !!!')
            return redirect('/')
        
        else:
            messages.success(
                request, f'login Error !!!! Provide Correct Username And Password')
    else:
        form = UserLoginForm()
        registerform = UserRegisterForm()
    return render(request, 'pages/login_register.html', {'form': form, 'registerform':registerform, 'all_category_qs':all_category_qs})

def user_register(request):
    all_category_qs = Category.objects.all()
    if request.method == 'POST':
        registerform = UserRegisterForm(request.POST)
        if registerform.is_valid():
            username = registerform.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Now Login')
            registerform.save()
            return redirect('/Oauth/')
    else:
        registerform = UserRegisterForm()
        form = UserLoginForm()
    return render(request, 'pages/login_register.html', { 'form':form, 'registerform':registerform, 'all_category_qs':all_category_qs })

def homepage(request):
    context = {}
    all_product_qs = Product.objects.all()
    all_category_qs = Category.objects.all()
    context['all_product_qs'] = all_product_qs
    context['all_category_qs'] = all_category_qs
    return render(request, 'pages/home.html', context)

def shop(request):
    context = {}
    all_product_qs = Product.objects.all()
    all_category_qs = Category.objects.all()
    context['all_product_qs'] = all_product_qs
    context['all_category_qs'] = all_category_qs
    return render(request, 'pages/shop.html', context)

def productdetails(request, id):
    context = {}
    try:
        all_category_qs = Category.objects.all()
        product_get_qs = Product.objects.get(pk = id)
        attr_qs = ProductAttribute.objects.filter(product_id = id)
        related_products = Product.objects.filter(category_id = product_get_qs.category_id)
        context['product_get_qs']=product_get_qs
        context['all_category_qs'] = all_category_qs
        context['attr_qs'] = attr_qs
        context['related_products'] = related_products
    except ObjectDoesNotExist:
        all_category_qs = Category.objects.all()
        return render(request, 'pages/404.html', {'all_category_qs':all_category_qs})
    
    return render(request, 'pages/product_detail.html', context)

def categorydetails(request, id):
    context = {}
    try:
        all_category_qs = Category.objects.all()
        category_get_qs = Category.objects.get(pk=id)
        all_product_qs = Product.objects.filter(category_id = id)
        context['category_get_qs']=category_get_qs
        context['all_product_qs'] = all_product_qs
        context['all_category_qs'] = all_category_qs
    except ObjectDoesNotExist:
        all_category_qs = Category.objects.all()
        return render(request, 'pages/404.html', {'all_category_qs':all_category_qs})

    return render(request, 'pages/category.html', context)

@login_required(login_url = '/Oauth/')
def user_profile(request):
    context = {}
    all_category_qs = Category.objects.all()
    context['all_category_qs'] = all_category_qs
    cart_list = Cart.objects.filter(user_id = request.user.id)
    context['cart_list'] = cart_list
    total = 0
    for x in cart_list:
        total += x.total

    order_list = Order.objects.filter(user_id = request.user.id)
    context['order_list'] = order_list
    context['cart_total'] = total

    return render(request, 'pages/profile.html', context)

def new(request, id, user = None):
    qs_get_product_to_cart = Product.objects.get(pk = id)
    user_obj = None
    if user is not None:
        if user.is_authenticated:
            user_obj = user

    return Cart.objects.create(
        user = request.user,
        product_id = qs_get_product_to_cart.id,
        total = qs_get_product_to_cart.product_price,
        ).save()
@login_required(login_url = '/Oauth/')
def add_to_shopping_cart(request, id):
    context = {}
    all_category_qs = Category.objects.all()
    context['all_category_qs'] = all_category_qs

    qs_get_product_to_cart = Product.objects.get(pk = id)

    qs = Cart.objects.filter(id = id)
    if qs.count() == 1:
        new_obj = False
        cart_obj = qs.first() 
        if request.user.is_authenticated and cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.qnty += 1
            cart_obj.save()
    else: 
        new(request,id)

    return redirect('/shop/')
@login_required(login_url = '/Oauth/')
def shopping_cart(request):
    context = {}
    all_category_qs = Category.objects.all()
    context['all_category_qs'] = all_category_qs

    cart_list = Cart.objects.filter(user_id = request.user.id)
    context['cart_list'] = cart_list
    total = 0
    for x in cart_list:
        total += x.total

    context['cart_total'] = total


    return render(request, 'pages/cart.html', context)

def remove_cart(request, id):
    qs_get_product_to_cart = Cart.objects.get(pk = id)
    qs_get_product_to_cart.delete()
    return redirect('/shopping/')

@login_required(login_url = '/Oauth/')
def checkout(request):
    context = {}
    all_category_qs = Category.objects.all()
    context['all_category_qs'] = all_category_qs

    cart_list = Cart.objects.filter(user_id = request.user.id)
    context['cart_list'] = cart_list
    total = 0
    for x in cart_list:
        total += x.total

    context['cart_total'] = total


    # ///////////////
    if cart_list.count() == 0:
        messages.success(request, f'No item In Cart { request.user.username }')
        return redirect('/shop/')
    if request.method == 'POST':
        order_obj = Order.objects.create(
            user = request.user,
            fname = request.POST['fname'],
            lname = request.POST['lname'],
            email = request.POST['email'],
            phone_number = request.POST['phone_number'],
            country = request.POST['country'],
            address = request.POST['address'],
            town_city = request.POST['town_city'],
            county_state = request.POST['county_state'],
            postal_zip = request.POST['postal_zip'],
        )
        
        order_obj.save()

    return render(request, 'pages/checkout.html', context)

def user_loguot(request):
    logout(request)
    messages.success(request, f'You Have logout !!!')
    return redirect('/Oauth/')
