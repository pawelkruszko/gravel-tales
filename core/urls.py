from django.urls import path

from .views import home, about

urlpatterns = [
    path("", home, name="site-home"),
    path("about/", about, name="site-about"),
]
