from django.db import models
from django.contrib.auth.models import AbstractUser

# Define choices for OfficerType
class OfficerRank(models.TextChoices):
    DUTYOFFICER = "DO", "Duty Officer"
    OCS = "OCS", "Officer in Charge of Station"
    ITOFFICER = "ITO", "Information Technology Officer"

# Define Officer model, extending AbstractUser
class Officer(AbstractUser):
    officer_rank = models.CharField(max_length=3, choices=OfficerRank.choices, default=OfficerRank.DUTYOFFICER)

    @property
    def is_ocs(self):
        return self.officer_rank == OfficerRank.OCS
    
    @property
    def is_itofficer(self):
        return self.officer_rank == OfficerRank.ITOFFICER
    
    @property
    def is_duty_officer(self):
        return self.officer_rank == OfficerRank.DUTYOFFICER

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Officer"
        verbose_name_plural = "Officers"
        ordering = ["username"]

# Define UserProfile model
class UserProfile(models.Model):
    user = models.OneToOneField(Officer, on_delete=models.CASCADE)
    # add any additional fields here
