from django.core.validators import RegexValidator
from django.db import models


class Subject(models.Model):
    """
    A Subject is equivalent to a LIGO detection event. A Subject may have multiple unique analysis pipelines
    """
    H1 = 1
    L1 = 2
    V1 = 4
    K1 = 8
    DETECTOR_CHOICES = (
        (H1, 'H1'),
        (L1, 'L1'),
        (V1, 'V1'),
        (K1, 'K1'),
    )

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
    detectors = models.IntegerField(default=0)

