from django.urls import path, include
from users import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerUser, name="register"),
]
