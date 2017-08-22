from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Product
from .forms import ProductForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def save_product_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            products = Product.objects.all()
            data['html_product_list'] = render_to_string('products/includes/partial_product_list.html', {
                'products': products
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
    else:
        form = ProductForm()
    return save_product_form(request, form, 'products/includes/partial_product_create.html')


def product_update(request, pk):
    product= get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
    else:
        form = ProductForm(instance=product)
    return save_product_form(request, form, 'products/includes/partial_product_update.html')


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    data = dict()
    if request.method == 'POST':
        product.delete()
        data['form_is_valid'] = True
        products = Product.objects.all()
        data['html_product_list'] = render_to_string('products/includes/partial_product_list.html', {
            'products': products
        })
    else:
        context = {'product': product}
        data['html_form'] = render_to_string('products/includes/partial_product_delete.html', context, request=request)
    return JsonResponse(data)
