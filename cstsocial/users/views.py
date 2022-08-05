from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def dashboard(request):
    return render(request, "users/dashboard.html")


@login_required(login_url="users:login")
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    context = {"profiles": profiles}
    return render(request, "users/profile_list.html", context)


@login_required(login_url="users:login")
def profile(request, id):
    profile = Profile.objects.get(id=id)
    if request.method == "POST":
        current_user = request.user.profile
        data = request.POST
        if data["add_friend"] == "Add":
            current_user.friends.add(profile)
        elif data["add_friend"] == "Remove":
            current_user.friends.remove(profile)
        current_user.save()
    context = {"profile": profile}
    return render(request, "users/profile.html", context)


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
