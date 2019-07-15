from django.shortcuts import render

from .forms import productform
from .models import product

# Create your views here.


def product_create_view(request):
    form = productform(request.POST or None)
    if form.is_valid():
        form.save()
        form = productform()

    context = {
        'form': form
    }
    return render(request, "product/create.html", context)


def product_detail_view(request):
    obj = product.objects.get(id=3)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, "product/detail.html", context)
