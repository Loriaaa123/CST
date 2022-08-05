from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerUser, name="register"),
    path("profile_list/", views.profile_list, name="profile_list"),
    path("profile/<int:id>/", views.profile, name="profile"),
    path("edit_profile/<int:id>/", views.edit_profile, name="edit_profile"),
    path("delete_user/<int:id>/", views.delete_user, name="delete_user"),
]
