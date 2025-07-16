from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_pages = request.GET.get('sort')
    phones = Phone.objects.all()
    if sort_pages == 'name':
        phones = phones.order_by('name')
    if sort_pages == 'min_price':
        phones = phones.order_by('price')
    if sort_pages == 'max_price':
        phones = phones.order_by('price').reverse()
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    product_object = Phone.objects.get(slug=slug)
    context = {'phone': product_object}
    return render(request, template, context)

