from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('rochelka', views.rochelka, name="rochelka"),
    path('<str:name>', views.greet, name="greet")
]