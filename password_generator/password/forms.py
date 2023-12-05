from django import forms
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm,PasswordResetForm,UserCreationForm
from django.contrib.auth.models import User


class CustomPasswordResetForm(PasswordResetForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    email = forms.EmailField(
            label="",
            required=True,
            widget = forms.EmailInput(attrs={
                "placeholder":"Valid Email",
                "type":"email",
                "name":"email",
                "class":"form-control",
                })
            )
    class Meta:
        model = User
        fields = ("email")

class CustomSetPasswordForm(SetPasswordForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    new_password1 = forms.CharField(
        label="",
        required=True,
        help_text="",
        widget = forms.PasswordInput(attrs={
            "placeholder":"password",
            "type":"password",
            "name":"password1",
            "class":"form-control",
            })
        )

    new_password2 = forms.CharField(
        label="",
        required=True,
        help_text="",
        widget = forms.PasswordInput(attrs={
            "placeholder":"confirm password",
            "type":"password",
            "name":"password1",
            "class":"form-control",
            })
        )

    class Meta:
        model = User
        fields = ("new_password1","new_password2")


class UserRegistrationForm(UserCreationForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)


    username = forms.CharField(
            label="",
            required=True,
            help_text="",
            widget = forms.TextInput(attrs={
                "placeholder":"username",
                "name":"username",
                "class":"username",
                "type":"text",
                })
            )

    email = forms.EmailField(
        label="",
        required=True,
        widget = forms.TextInput(attrs={
            "placeholder":"Email",
            "type":"email",
            "name":"email",
            "class":"email",
            })
        )

    password1 = forms.CharField(
        label="",
        required=True,
        help_text="",
        widget = forms.PasswordInput(attrs={
            "placeholder":"password",
            "type":"password",
            "name":"password1",
            "class":"password",
            })
        )
    
    password2 = forms.CharField(
        label="",
        required=True,
        help_text="",
        widget = forms.PasswordInput(attrs={
            "placeholder":"confirm password",
            "type":"password",
            "name":"password1",
            "class":"password",
            })
        )

    class Meta:
        model = User
        fields = ("email","username")

