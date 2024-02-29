from django.contrib import admin
from .models import Officer, UserProfile

@admin.register(Officer)
class OfficerAdmin(admin.ModelAdmin):
    list_display = ("username", "get_officer_rank_display")