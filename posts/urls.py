from django.urls import path

from . import views

urlpatterns = [
    path("homepage/", views.homepage, name="page_home"),
]