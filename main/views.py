from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.core import serializers
from main.models import Products
from main.forms import ProductsForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

def show_main(request):
    context = {
        'project_name': 'Athletica Sportsware',
        'name': 'Ahmad Omar Mohammed Maknoon',
        'npm': '2406419612',
        'class': 'PBP D'
    }
    return render(request, 'main.html', context)

def show_json(request):
    data = Products.objects.all()
    data_json = serializers.serialize("json", data)
    return HttpResponse(data_json, content_type="application/json")

def show_xml(request):
    data = Products.objects.all()
    data_xml = serializers.serialize("xml", data)
    return HttpResponse(data_xml, content_type="application/xml")

def show_xml_byID(request, id):
    try:
        product = Products.objects.filter(pk=id)
        xml_data = serializers.serialize("xml", product)
        return HttpResponse(xml_data, content_type="application/xml")
    except Products.DoesNotExist:
        return HttpResponse(status=404)

def show_json_byID(request, id):
    try:
        product = Products.objects.filter(pk=id)
        json_data = serializers.serialize("json", product)
        return HttpResponse(json_data, content_type="application/json")
    except Products.DoesNotExist:
        return HttpResponse(status=404)

@login_required(login_url=reverse_lazy('main:login'))
def add_product(request):
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, 'Product added successfully!')
            return redirect('main:products')
        else:
            # Kalau form ga valid, print error buat debug
            print("Form errors:", form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProductsForm()
    
    context = {'form': form}
    return render(request, "create_product.html", context)

def show_products(request):
    filter_type = request.GET.get('filter', 'all')
    filter_gender = request.GET.get('gender', 'all')
    filter_sport = request.GET.get('sport', 'all')
    filter_category = request.GET.get('category', 'all')
    
    result = ""
    
    # Filter by ownership
    if filter_type == "all":
        products = Products.objects.all()
        result = "All Products"
    else:
        products = Products.objects.filter(user=request.user)
        result = "My Products"
    
    # Filter by gender
    if filter_gender != "all":
        products = products.filter(gender=filter_gender)
        result += " / " + filter_gender.capitalize()
    
    # Filter by sport
    if filter_sport != "all":
        products = products.filter(product_group=filter_sport)
        result += " / " + filter_sport.capitalize()

    # Filter by category
    if filter_category != "all":
        products = products.filter(category=filter_category)
        result += " / " + filter_category.capitalize()

    context = {
        'products': products,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'filter_display': result,
        'current_filter': filter_type
    }
    
    # Return partial for AJAX requests
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'products_partial.html', context)
    
    return render(request, 'mainpage.html', context)

def show_homepage(request):
    # Get featured products
    featured_products = Products.objects.filter(is_featured=True)[:8]
    
    # Get all products
    products = Products.objects.all()[:12]

    context = {
        'featured_products': featured_products,
        'products': products,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }

    return render(request, 'homepage.html', context)

def product_detail(request, id):
    product = get_object_or_404(Products, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse('main:homepage'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            messages.success(request, f'Welcome back, {user.username}!')
            return response
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm(request)

    context = {'form': form}
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:homepage'))
    response.delete_cookie('last_login')
    messages.info(request, 'You have been logged out successfully.')
    return response

@login_required(login_url=reverse_lazy('main:login'))
def user_cart(request):
    return HttpResponse('Cart feature is under development...')

@login_required(login_url=reverse_lazy('main:login'))
def edit_product(request, id):
    product = get_object_or_404(Products, pk=id, user=request.user)
    
    if request.method == "POST":
        form = ProductsForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('main:products')
        else:
            print("Form errors:", form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProductsForm(instance=product)
    
    context = {'form': form}
    return render(request, "edit_product.html", context)

@login_required(login_url=reverse_lazy('main:login'))
def delete_product(request, id):
    product = get_object_or_404(Products, pk=id, user=request.user)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('main:products')

# AJAX VIEWS

@login_required(login_url=reverse_lazy('main:login'))
@require_POST
def add_product_ajax(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            name = request.POST.get('name')
            price = request.POST.get('price')
            description = request.POST.get('description', '')
            detail = request.POST.get('detail', '')
            category = request.POST.get('category')
            product_group = request.POST.get('product_group')
            gender = request.POST.get('gender')
            size = request.POST.get('size')
            stock_quantity = request.POST.get('stock_quantity', 0)
            is_featured = request.POST.get('is_featured') == 'on'
            thumbnail = request.POST.get('thumbnail', '')
            
            # Validation
            if not name or not price:
                return JsonResponse({'success': False, 'error': 'Name and price are required'})
            
            # Create product
            product = Products.objects.create(
                user=request.user,
                name=name,
                price=int(price),
                description=description,
                detail=detail,
                category=category,
                product_group=product_group,
                gender=gender,
                size=size,
                stock_quantity=int(stock_quantity) if stock_quantity else 0,
                is_featured=is_featured,
                thumbnail=thumbnail if thumbnail else 'https://via.placeholder.com/300'
            )
            
            return JsonResponse({'success': True, 'product_id': str(product.id)})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})
# 

@login_required(login_url=reverse_lazy('main:login'))
@require_POST
def update_product_ajax(request, id):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            product = Products.objects.get(id=id, user=request.user)
            
            name = request.POST.get('name')
            price = request.POST.get('price')
            
            # Validation
            if not name or not price:
                return JsonResponse({'success': False, 'error': 'Name and price are required'})
            
            product.name = name
            product.price = int(price)
            product.description = request.POST.get('description', '')
            product.category = request.POST.get('category')
            product.product_group = request.POST.get('product_group')
            product.gender = request.POST.get('gender')
            product.size = request.POST.get('size')
            product.stock_quantity = int(request.POST.get('stock_quantity', 0))
            product.is_featured = request.POST.get('is_featured') == 'on'
            
            thumbnail = request.POST.get('thumbnail', '')
            if thumbnail:
                product.thumbnail = thumbnail
            
            product.save()
            
            return JsonResponse({'success': True})
        except Products.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Product not found or you do not have permission to edit it'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})

@login_required(login_url=reverse_lazy('main:login'))
@require_POST
def delete_product_ajax(request, id):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            product = Products.objects.get(id=id, user=request.user)
            product.delete()
            
            return JsonResponse({'success': True})
        except Products.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Product not found or you do not have permission to delete it'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})

def products_partial(request):
    """AJAX endpoint to get products HTML partial"""
    filter_type = request.GET.get('filter', 'all')
    filter_gender = request.GET.get('gender', 'all')
    filter_sport = request.GET.get('sport', 'all')
    filter_category = request.GET.get('category', 'all')
    
    # Filter by ownership
    if filter_type == "all":
        products = Products.objects.all()
    else:
        if request.user.is_authenticated:
            products = Products.objects.filter(user=request.user)
        else:
            products = Products.objects.none()
    
    # Filter by gender
    if filter_gender != "all":
        products = products.filter(gender=filter_gender)
    
    # Filter by sport
    if filter_sport != "all":
        products = products.filter(product_group=filter_sport)

    # Filter by category
    if filter_category != "all":
        products = products.filter(category=filter_category)

    context = {
        'products': products,
        'current_filter': filter_type
    }
    
    return render(request, 'products_partial.html', context)