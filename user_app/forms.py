from django import forms
from django.contrib.auth.forms import UserCreationForm
from user_app.models import Officer, UserProfile


class OfficerRegistrationForm(UserCreationForm):
    class Meta:
        model = Officer
        fields = (
            "first_name",
            "last_name",
            "username",
            "officer_rank",
            "email",
            "password1",
            "password2",
        )
        labels = {"username": "Badge Number"}
        widgets = {
            "officer_rank": forms.RadioSelect(attrs={"class": "form-check"}),
        }
