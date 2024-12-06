from django import forms

from apps.base.models import CustomUser


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email", "name", "surname", "address", "phone", "user_type")
