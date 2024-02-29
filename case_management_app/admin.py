from django.contrib import admin
from .models import Case, Evidence, Victim, Reporter


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


@admin.register(Victim)
class VictimAdmin(admin.ModelAdmin):
    list_display = ("victim_name", "victim_phone_number", "victim_email")
    search_fields = ("victim_name", "victim_phone_number", "victim_email")


@admin.register(Reporter)
class ReporterAdmin(admin.ModelAdmin):
    list_display = ("reporter_name", "reporter_phone_number", "reporter_email")
    search_fields = ("reporter_name", "reporter_phone_number", "reporter_email")
