from . import views 
from django.urls import path

urlpatterns = [
    path("Test/", views.print_hello),  
]