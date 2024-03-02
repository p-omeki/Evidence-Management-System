from django.contrib import admin
from .models import Case, Evidence, Complainant


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ("serial_number", "case_title", "case_officer", "created_at")
    search_fields = ("serial_number", "case_title", "case_officer", "created_at")
    list_filter = ("case_officer", "created_at")


@admin.register(Evidence)
class EvidenceAdmin(admin.ModelAdmin):
    list_display = ("type", "description", "case")
    search_fields = ("type", "description", "case")
    list_filter = ("case",)


@admin.register(Complainant)
class ComplainantAdmin(admin.ModelAdmin):
    list_display = ("complainant_name", "complainant_phone_number", "complainant_email")
    search_fields = ("complainant_name", "complainant_phone_number", "complainant_email")

