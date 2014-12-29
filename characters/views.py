from django.shortcuts import get_object_or_404, render

from characters.models import Character


def index(request):
    all_characters = Character.objects.all()
    context = {'all_characters': all_characters}
    return render(request, 'characters/index.html', context)


def view_character(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    context = {'character': character}
    return render(request, 'characters/view_character.html', context)
