from django.shortcuts import render

# Create your views here.

'''
python function is a view.
1. first parameter is a request, which is a class object for httprequest
'''
from django.http import HttpRequest
from django.http import HttpResponse


# we are looking for users to use
def index(request):
    pass

# def index(request)
#
#     return HttpResponse('ok')

