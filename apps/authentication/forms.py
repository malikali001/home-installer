from django import forms
from django.contrib.auth.forms import UserCreationForm

from apps.base.models import CustomUser


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "email", "class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )


class SignUpForm(UserCreationForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Name", "class": "form-control"}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"})
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Phone Number", "class": "form-control"}
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password check", "class": "form-control"}
        )
    )

    class Meta:
        model = CustomUser
        fields = ("name", "email", "phone", "password1", "password2")
