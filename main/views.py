from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.models import Products, Color
from main.forms import ProductsForm

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


def add_product(request):
    form = ProductsForm(request.POST or None)

    if(form.is_valid() and request.method == "POST"):
        form.save()
        return redirect('main:products')
    
    context = {'form': form}
    return render(request, "create_product.html", context)
    
def show_products(request):
    products = Products.objects.all()
    context = {
        'products':products
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

