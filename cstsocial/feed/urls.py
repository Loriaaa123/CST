from django.urls import path
from users import views

app_name = "feed"
urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("post_detail/<int:id>/", views.post_detail, name="post_detail"),
]
