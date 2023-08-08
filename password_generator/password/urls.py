from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name="index"),
        path("signin/", views.signin, name="signin"), 
        path("signup/", views.signup, name="signup"), 
        path("logout/", views.logout, name="logout"), 
        path("display_password/<str:username>", views.dis_pass, name="dis_pass"),
        path("view_password/<str:username>", views.view_pass, name="view_pass"),
        path("recover_password/", views.forgotten, name="forgotten"),
        path("update_Password/", views.update, name="update_pass"), 
        ]
