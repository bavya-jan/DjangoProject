from django.shortcuts import render
from django.http import HttpResponse,JsonResponse, HttpResponseRedirect
from .forms import LoginForm, RegisterForm
from .models import UserDetails

# Create your views here.
def print_hello(request):
    return HttpResponse("Hello, World!")

def login_view(request):
    if request.session.get("username"):
        return HttpResponse("You are already logged in")
    if request.method == "POST":
        try:
            login_form = LoginForm(request.POST, request.POST)
            if login_form.is_valid():
                # Retrieve user object from form data
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                
                user = UserDetails.objects.get(username=username)
                if user.password == password:
                    # Perform authentication
                    request.session["username"] = username
                    return JsonResponse({"success": True, "message": "Login successful"})
                else:
                    return JsonResponse({"success": False, "message": "Incorrect password"})
                # return JsonResponse({"success": True, "message": "Login successful"})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    else:
        login_form = LoginForm()
        return render(request, "Loginify/Login.html", {"login_form": login_form})
        

def register_view(request):
    if request.method == "POST":
        try:
            register_form = RegisterForm(request.POST, request.POST, request.POST)
            if register_form.is_valid():
                username = register_form.cleaned_data["username"]
                email = register_form.cleaned_data["email"]
                password = register_form.cleaned_data["password"]
                
                if UserDetails.objects.filter(email=email).exists():  
                    return JsonResponse({"success": False, "message": "User already exists"})
                else:
                    user_details = UserDetails(username=username, email=email, password=password)
                    user_details.save()
                    login_form = LoginForm()
                    return render(request, "Loginify/Login.html", {"login_form": login_form})
                
                # register_form.save()
                # return JsonResponse({"success": True, "message": "Login successful"})
                
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    else:
        register_form = RegisterForm()
        return render(request, "Loginify/Register.html", {"register_form": register_form})

