from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world.  You're at the Characters index.")


def view_character(request, character_id):
    return HttpResponse("You're looking at character %s." % character_id)
