from django.http import HttpResponse
from django.shortcuts import render

from characters.models import Character


def index(request):
    all_characters = Character.objects.all()
    output = '<br>'.join([character.name for character in all_characters])
    return HttpResponse(output)


def view_character(request, character_id):
    character = Character.objects.get(id=character_id)
    return HttpResponse(character)
