from django import forms
from .models import Exercises

class ExercisesForm(forms.ModelForm):
    class meta:
        model = Exercises
        fields = ['name', 'reps','sets']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Exercises.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError('Record with this name exists.')
        return name    