from django import forms
from .models import Questionnaire

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = ['nom', 'age', 'genre', 'satisfaction']


class VotreFormulaire(forms.Form):
    feature1 = forms.CharField(label='Feature 1', max_length=100)
    feature2 = forms.CharField(label='Feature 2', max_length=100)
