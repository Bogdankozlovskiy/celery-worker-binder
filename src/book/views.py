from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from book.tasks import mul


@cache_page(2)
def hello(request):
	result = mul.delay(3, 4)
	return HttpResponse(f"hello world {result.get()}")
# Create your views here.
