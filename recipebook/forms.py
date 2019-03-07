from django import forms
from recipebook.models import Author


class AddAuthor(forms.Form):
    name = forms.CharField(label='Author Name', max_length=100)
    bio = forms.CharField(widget=forms.Textarea, label='bio')


class AddRecipe(forms.Form):
    title = forms.CharField(label='Recipe Title', max_length=100)
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(), label='Author')
    description = forms.CharField(max_length=150, label="Description")
    time = forms.IntegerField(label='Prep Duration')
    instructions = forms.CharField(widget=forms.Textarea, label="Instructions")
