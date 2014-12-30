from django import forms

from characters.models import Character


class CharacterForm(forms.ModelForm):

    class Meta:
        model = Character
        fields = ['name', 'background', 'race', 'cclass', 'alignment',
                'strength', 'dexterity', 'constitution', 'intelligence',
                'wisdom', 'charisma', 'max_hit_points']

    def __init__(self, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)
        for field in ['strength', 'dexterity', 'constitution', 'intelligence',
                'wisdom', 'charisma', 'max_hit_points']:
            self.fields[field].widget.attrs['readonly'] = True
