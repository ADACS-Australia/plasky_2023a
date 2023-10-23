from django.core.validators import RegexValidator
from django.db import models
from django.db.models import UniqueConstraint, Q


class Subject(models.Model):
    event_id = models.CharField(
        max_length=15,
        blank=False,
        null=False,
        unique=True,
        validators=[RegexValidator(regex=r"^GW\d{6}_\d{6}$", message="Must be of the form GW123456_123456")],
    )
    trigger_id = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[RegexValidator(regex=r"^S\d{6}[a-z]{1,2}$", message="Must be of the form S123456a")],
    )
    gps_time = models.FloatField(default=1126259462.391)

    # Detector configuration
    h1 = models.BooleanField(default=False)
    l1 = models.BooleanField(default=False)
    v1 = models.BooleanField(default=False)
    k1 = models.BooleanField(default=False)

