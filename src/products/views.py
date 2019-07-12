from django.shortcuts import render

from products.models import product
# Create your views here.


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
