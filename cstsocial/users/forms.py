from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "input"})


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["friends", "user"]
        widgets = {
            "bio": forms.Textarea(attrs={"class": "input", "rows": "3"}),
            "private_profile": forms.CheckboxInput(),
        }
