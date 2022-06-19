from django import forms
from .models import LearnWithYourKids


class LearnWithYourKidsForm(forms.ModelForm):
    class Meta:
        model = LearnWithYourKids
        fields = ("title", "description", "url", "photo")
