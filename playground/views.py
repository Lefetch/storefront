from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import  Product


def say_hello(request):
    try:
        # check if record exists before get value
        exists = Product.objects.filter(pk=0).exists()
        if not exists:
            return HttpResponse('Not Found!')
        product = Product.objects.get(pk=1)
        # keyword=value
        queryset = Product.objects.filter(price__gt=50)
    except ObjectDoesNotExist:
        pass
    return HttpResponse("Hello World!")
