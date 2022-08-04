from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def dashboard(request):
    return render(request, "users/dashboard.html")


def registerUser(request):
    page = "register"
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "You have successfully registered")
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid form")
            return redirect("register")
    context = {"page": page, "form": form}
    return render(request, "registration/login_register.html", context)


def loginUser(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        username = request.POST["username"].lower()
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User not found")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")
    context = {"page": page}
    return render(request, "registration/login_register.html", context)


def logoutUser(request):
    logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect("login")
