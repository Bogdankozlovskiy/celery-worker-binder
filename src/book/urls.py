from django.urls import path
from book.views import hello


urlpatterns = [
	path("", hello)
]