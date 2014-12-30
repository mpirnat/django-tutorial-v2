from django import forms


class CharacterForm(forms.Form):

    name = forms.CharField(max_length=200)
    background = forms.CharField()
