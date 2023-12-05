from django.contrib import admin
from django.urls import path, include
from password.forms import CustomPasswordResetForm,CustomSetPasswordForm
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("password.urls")),
    path(
        "password_reset_view/",
        auth_views.PasswordResetView.as_view(
            template_name="password_reset.html",
            form_class=CustomPasswordResetForm),
        name="password_reset"),

    path(
        "password_reset_done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="password_reset_done.html"),
        name="password_reset_done"),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password_reset_confirm.html",
            form_class=CustomSetPasswordForm),
        name="password_reset_confirm"),
    path(
        "password_reset_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password_reset_complete.html"),
        name="password_reset_complete")
]
