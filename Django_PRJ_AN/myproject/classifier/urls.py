
from django.urls import path
from .views import classify
from .views import display

urlpatterns = [
    #path("classify/", classify, name="classify"),
    path("", classify, name="classify"),
    path("display/", display, name="display"),
]
