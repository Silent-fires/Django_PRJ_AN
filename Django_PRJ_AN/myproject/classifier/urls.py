
from django.urls import include, path
from django.contrib import admin
from .views import classify
from .views import display

urlpatterns = [
    path("", classify, name="classify"),
    path("display/", display, name="display"),
    path("api/", include("myproject.api.urls")),
    path('admin/', admin.site.urls),
]
