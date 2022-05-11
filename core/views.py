from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('The url setup worked perfectly! <a href="store/product/0">Go to product.</a>')

