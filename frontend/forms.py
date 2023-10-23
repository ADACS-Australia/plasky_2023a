from django.core.exceptions import ValidationError
from django.forms import ModelForm, CheckboxInput

from frontend.models import Subject


DETECTORS = ["h1", "l1", "v1", "k1"]
CheckboxInput


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ["event_id", "gps_time"] + DETECTORS

    def clean(self):
        cleaned_data = super().clean()

        detector_valid = any(cleaned_data[detector] for detector in DETECTORS)

        if not detector_valid:
            raise ValidationError(
                "At least one detector must be selected"
            )
