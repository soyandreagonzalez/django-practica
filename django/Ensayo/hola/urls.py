from django.urls import path
from hola import views
urlpatterns = [
    path("", views.home, name="home"),
]