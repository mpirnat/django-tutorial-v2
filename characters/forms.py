from django import forms

from characters.models import Character


class CharacterForm(forms.ModelForm):

    class Meta:
        model = Character
