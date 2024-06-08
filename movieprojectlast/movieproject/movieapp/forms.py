from django import forms

from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title','description','poster','date','actors','category']

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ['rating','comment']


