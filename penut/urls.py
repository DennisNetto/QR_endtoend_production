from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path("createqr/", views.createqr, name="create"),
    path("create1/", views.create1, name="create1"),

]
