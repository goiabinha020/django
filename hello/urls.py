from django.urls import path
from . import views
urlpatterns=[
    path("", views.index, name = "index"),
    path("<str:name>", views.greet, name = "greet "),
    path("gui", views.eu, name = "guilherme"),
    path("lucas", views.lucas, name = "lucas")
    ]
