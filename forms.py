from django import forms
from .models import quiz
class QuizForm(forms.Form):
   userans=forms.CharField(label='your answer',max_length=20)
        
