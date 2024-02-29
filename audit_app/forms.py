from django import forms
from .models import AuditTrail

class AuditTrailForm(forms.ModelForm):
    class Meta:
        model = AuditTrail
        fields = "__all__"
        widgets = {
            "user": forms.Select(attrs={"class": "form-control"}),
            "action": forms.TextInput(attrs={"class": "form-control"}),
            "date": forms.DateTimeInput(attrs={"class": "form-control"}),
            "ip_address": forms.TextInput(attrs={"class": "form-control"}),
            "user_agent": forms.TextInput(attrs={"class": "form-control"}),
        }