from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
        path("", views.index, name="index"),
        path("signup/",views.signup,name="signup"),
        path("signin/",views.signin,name="login"),
        path("logout/",auth_views.LogoutView.as_view(),name="logout"),
        path("display_password/<str:username>", views.dis_pass, name="dis_pass"),
        path("view_password/<str:username>", views.view_pass, name="view_pass"), 
        ]
