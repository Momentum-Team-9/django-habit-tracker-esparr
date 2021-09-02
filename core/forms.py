from django import forms
from django.forms import fields
from .models import DailyRecord, Habit


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'title',
            'goal',
        ]


class DailyRecordForm(forms.ModelForm):
    class Meta:
        model = DailyRecord
        fields = [
            'habit',
        ]
