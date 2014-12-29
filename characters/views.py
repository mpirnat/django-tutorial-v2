from django.http import Http404
from django.shortcuts import render

from characters.models import Character


def index(request):
    all_characters = Character.objects.all()
    context = {'all_characters': all_characters}
    return render(request, 'characters/index.html', context)


def view_character(request, character_id):
    try:
        character = Character.objects.get(id=character_id)
    except Character.DoesNotExist:
        raise Http404

    context = {'character': character}
    return render(request, 'characters/view_character.html', context)
