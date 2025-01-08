
from django.urls import path
from. import views

urlpatterns = [
    path("Test/", views.print_hello),  
    path("Login/", views.login_view),
    path("Register/", views.register_view),
]