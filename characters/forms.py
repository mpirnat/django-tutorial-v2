from django import forms

from characters.models import Character


class CharacterForm(forms.ModelForm):

    class Meta:
        model = Character
        fields = ['name', 'background', 'race', 'cclass', 'alignment']
