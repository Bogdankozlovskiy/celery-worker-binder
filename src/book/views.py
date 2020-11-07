from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import cache_page


@cache_page(2)
def hello(request):
	return HttpResponse("hello world")
# Create your views here.
