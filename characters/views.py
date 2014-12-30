from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from characters.forms import CharacterForm
from characters.models import Character, Class, Race


class CharacterIndexView(generic.ListView):

    template_name = 'characters/index.html'
    context_object_name = 'all_characters'  # better than 'object_list'

    def get_queryset(self):
        return Character.objects.all()


class CharacterDetailView(generic.DetailView):

    model = Character
    template_name = 'characters/view_character.html'


def create_character(request):
    form = CharacterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        character = Character(
                name=request.POST['name'],
                background=request.POST['background'],
                race_id=1,
                cclass_id=1
        )
        character.save()

        return redirect('characters:view', character_id=character.id)

    context = {'form': form}
    return render(request, 'characters/create_character.html', context)
