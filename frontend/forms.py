from functools import reduce

from django.core.exceptions import ValidationError
from django import forms

from frontend.models import Subject


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        exclude = ["trigger_id", "detectors"]

    event_id = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'GW123456_123456'}
        )
    )

    gps_time = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': '1126259462.391'}
        )
    )

    detector_multi = forms.TypedMultipleChoiceField(
        coerce=int,
        choices=Subject.DETECTOR_CHOICES,
        required=True,
        widget=forms.CheckboxSelectMultiple()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['detector_multi'].initial = [
            c for c, _ in Subject.DETECTOR_CHOICES
            if self.instance.detectors & c
        ]

    def save(self, *args, **kwargs):
        cleaned_data = super().clean()
        self.instance.detectors = reduce(
            lambda x, y: x | y,
            cleaned_data.get('detector_multi', []),
            0)

        return super().save(*args, **kwargs)

