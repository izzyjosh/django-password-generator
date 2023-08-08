from django import forms
from django.contrib.auth.forms import PasswordChangeForm


class ForgottenPassword(forms.Form):
    username = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder":"username", "class":"user_data"}), 
            label=False, 
            max_length=30)
    email = forms.CharField(
            widget=forms.EmailInput(
                attrs={
                    "placeholder":"email", "class":"user_data"}), 
            label=False, )


class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["old_password"].widget=forms.PasswordInput(attrs={
            "class":"user_data","placeholder":"old password"})
        self.fields["old_password"].label=False
        self.fields["new_password1"].widget=forms.PasswordInput(attrs={
            "class":"user_data","placeholder":"new password"})
        self.fields["new_password1"].label=False
        self.fields["new_password2"].widget=forms.PasswordInput(attrs={
            "class":"user_data","placeholder":"new password"})
        self.fields["new_password2"].label=False



