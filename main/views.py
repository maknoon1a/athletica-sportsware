from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.core import serializers
from main.models import Products, Color
from main.forms import ProductsForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, aauthenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime

# Create your views here.
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

def show_json_byID(request, id):
    data = Products.objects.get(pk=id)
    data_json = serializers.serialize("json", [data])
    return HttpResponse(data_json, content_type="application/json")

def show_xml_byID(request, id):
    data = Products.objects.get(pk=id)
    data_xml = serializers.serialize("xml", [data])
    return HttpResponse(data_xml, content_type="application/xml")

@login_required(login_url=reverse_lazy('main:login'))
def add_product(request):
    form = ProductsForm(request.POST or None)

    if(form.is_valid() and request.method == "POST"):
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        form.save_m2m()
        return redirect('main:homepage')
    
    context = {'form': form}
    return render(request, "create_product.html", context)
    
def show_products(request):
    filter_type = request.GET.get('filter', 'all')
    
    if filter_type == "all":
        products = Products.objects.all()
    else:
        products = Products.objects.filter(user=request.user)
    
    context = {
        'products':products,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, 'show_products.html', context)

def product_detail(request, id):
    product = get_object_or_404(Products, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)


def show_color(request):
    colors = Color.objects.all()
    json_colors = serializers.serialize("json", colors)
    return HttpResponse(json_colors, content_type="application/json")


def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Your account has been successfully created!')
            form.save()
            return redirect('main:login')
    else:
        form = UserCreationForm()

    context = {'form':form}
    return render(request, 'register.html', context)


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            response = HttpResponseRedirect(reverse('main:homepage'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            login(request, user)
            return response
    else:
        form = AuthenticationForm(request)

    context = {'form':form}
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:homepage'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url=reverse_lazy('main:login'))
def user_cart(request):
    return HttpResponse('Proses Pengembangan...')

