from django.db import models
from django.utils import timezone
from django.conf import settings


class Complainant(models.Model):
    case = models.ForeignKey(
        "Case", on_delete=models.CASCADE, related_name="complainants", null=True, blank=True
    )
    complainant_name = models.CharField(max_length=255, default="No name provided")
    complainant_phone_number = models.CharField(max_length=20, default="No contact provided")
    complainant_email = models.EmailField(max_length=255, default="No email provided")
    complainant_statement = models.TextField(default="No statement provided")

    def __str__(self):
        return f"{self.complainant_name} - {self.complainant_phone_number}"

    class Meta:
        verbose_name = "Complainant"
        verbose_name_plural = "Complainants"


class Case(models.Model):
    serial_number = models.AutoField(primary_key=True, null=False, blank=True)
    case_title = models.CharField(max_length=255, default="No title provided")
    case_description = models.TextField(default="No description provided")
    case_officer = models.ForeignKey(
        "user_app.Officer",
        on_delete=models.CASCADE,
        related_name="cases",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    case_status = models.CharField(
        max_length=255,
        choices=[
            ("Open", "Open"),
            ("Closed", "Closed"),
            ("Appealed", "Appealed"),
        ],
        default="Open",
        blank=True,
    )
    case_outcome = models.CharField(
        max_length=255,
        choices=[("Pending", "Pending"), ("Resolved", "Resolved")],
        default="Pending",
        blank=True,
    )
    case_verdict = models.CharField(
        max_length=255,
        choices=[
            ("Pending", "Pending"),
            ("Guilty", "Guilty"),
            ("Not Guilty", "Not Guilty"),
            ("Dismissed", "Dismissed"),
            ("Settled", "Settled"),
        ],
        default="Pending",
        blank=True,
    )
    # Restore case
    disposed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.serial_number} - {self.case_title}"

    class Meta:
        verbose_name = "Case"
        verbose_name_plural = "Cases"
        ordering = ["serial_number"]


class Evidence(models.Model):
    case = models.ForeignKey(
        Case,
        on_delete=models.CASCADE,
        related_name="evidences",
        to_field="serial_number",
    )
    type = models.CharField(max_length=255, default="No type provided")
    description = models.TextField(default="No description provided")
    case_officer = models.ForeignKey(
        "user_app.Officer", on_delete=models.CASCADE, related_name="evidences"
    )

    # evidence state details
    is_collected = models.BooleanField(default=True)
    is_analysed = models.BooleanField(default=False)
    is_presented = models.BooleanField(default=False)
    is_disposed = models.BooleanField(default=False)

    # collection details
    collected_on = models.DateField(default=timezone.now)
    collected_by = models.ForeignKey(
        "user_app.Officer", on_delete=models.CASCADE, related_name="collected_evidences"
    )
    collection_details = models.TextField(default="No details provided")

    # analysis details
    analysed_on = models.DateField(null=True, blank=True)
    analysed_by = models.ForeignKey(
        "user_app.Officer",
        on_delete=models.CASCADE,
        related_name="analysed_evidences",
        null=True,
        blank=True,
    )
    analysis_details = models.TextField(null=True, blank=True)

    # presentation details
    presented_on = models.DateField(null=True, blank=True)
    presented_by = models.ForeignKey(
        "user_app.Officer",
        on_delete=models.CASCADE,
        related_name="presented_evidences",
        null=True,
        blank=True,
    )
    presentation_details = models.TextField(null=True, blank=True)

    # disposal details
    disposed_on = models.DateField(null=True, blank=True)
    disposed_by = models.ForeignKey(
        "user_app.Officer",
        on_delete=models.CASCADE,
        related_name="disposed_evidences",
        null=True,
        blank=True,
    )
    disposal_details = models.TextField(null=True, blank=True)
    disposal_reason = models.CharField(max_length=255, null=True, blank=True)
    disposal_method = models.CharField(max_length=255, null=True, blank=True)
   

    
    # soft delete
    disposed = models.BooleanField(default=False)
    disposed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"Evidence {self.type} on case {self.case.serial_number}"

    class Meta:
        verbose_name = "Evidence"
        verbose_name_plural = "Evidences"
        ordering = ["case"]
