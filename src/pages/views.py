from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    # return HttpResponse("<h1>Hello world<h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def share_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "This_is_true": True,
        "my_number": 123,
        "my_list": [1234, 142, 424, "Abc"]
    }
    return render(request, "share.html", my_context, {})


def view_view(request, *args, **kwargs):
    return render(request, "view.html", {})
