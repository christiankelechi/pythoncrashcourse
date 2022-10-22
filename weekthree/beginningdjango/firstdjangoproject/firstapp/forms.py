from turtle import width
from django import forms
from .models import Fruit

class FruitPost(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Name of the fruit"}))
    color=forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Color of the fruit"}))
    description=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter description'}))
    class Meta:
        model=Fruit
        fields=['name','color','description']