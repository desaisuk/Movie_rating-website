from django import forms
from .models import MovieReview

class RatingForm(forms.ModelForm):

    class Meta:
        model = MovieReview
        fields = ['title', 'rating', 'comment']
        widgets = {'title': forms.HiddenInput()}
    
        

