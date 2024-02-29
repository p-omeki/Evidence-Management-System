from django.shortcuts import render
from .models import AuditTrail

# Create your views here.

def audit_logs(request):
    logs = AuditTrail.objects.all().order_by("date")
    return render(request, "audit_logs.html", {"logs": logs})
