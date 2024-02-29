from django.urls import path
from . import views

app_name = "audit_app"

urlpatterns = [
    path("audit_logs/", views.audit_logs, name="audit_logs"),
]
