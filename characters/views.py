from django.shortcuts import get_object_or_404, redirect, render

from characters.forms import CharacterForm
from characters.models import Character, Class, Race


def index(request):
    all_characters = Character.objects.all()
    context = {'all_characters': all_characters}
    return render(request, 'characters/index.html', context)


def view_character(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    context = {'character': character}
    return render(request, 'characters/view_character.html', context)


def create_character(request):
    form = CharacterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        race = Race.objects.get(id=1)
        cclass = Class.objects.get(id=1)

        character = Character(
                name=request.POST['name'],
                background=request.POST['background'],
                race=race,
                cclass=cclass
        )
        character.save()

        return redirect('characters:view', character_id=character.id)

    context = {'form': form}
    return render(request, 'characters/create_character.html', context)
