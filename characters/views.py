from django.http import HttpResponse
from django.shortcuts import render

from characters.models import Character


def index(request):
    all_characters = Character.objects.all()
    context = {'all_characters': all_characters}
    return render(request, 'characters/index.html', context)


def view_character(request, character_id):
    character = Character.objects.get(id=character_id)
    return HttpResponse(character)
