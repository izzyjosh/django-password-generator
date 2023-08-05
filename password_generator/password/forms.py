from django import forms

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


class UpdatePassword(forms.Form):
    username = forms.CharField(
            widget=forms.TextInput(attrs={
                "placeholder":"username", "class":"user_data"}), 
            label=False, 
            max_length=30)
    password = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "placeholder":"password", "class":"user_data"}), 
                label=False,)
    confirm_password = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "placeholder":"confirm_password", "class":"user_data"}),
                label=False,)
