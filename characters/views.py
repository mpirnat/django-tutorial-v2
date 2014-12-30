from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from characters.forms import CharacterForm
from characters.models import Character, Class, Race


class CharacterIndexView(ListView):

    template_name = 'characters/index.html'
    context_object_name = 'all_characters'  # better than 'object_list'

    def get_queryset(self):
        return Character.objects.all().order_by('name')


class CharacterDetailView(DetailView):

    model = Character
    template_name = 'characters/view_character.html'


class CharacterCreationView(CreateView):

    model = Character
    template_name = 'characters/create_character.html'
    form_class = CharacterForm

    def get_success_url(self):
        return reverse('characters:view', kwargs={'pk': self.object.pk})


class CharacterUpdateView(UpdateView):

    model = Character
    form_class = CharacterForm
    template_name = 'characters/update_character.html'

    def get_success_url(self):
        return reverse('characters:view', kwargs={'pk': self.object.pk})


class CharacterDeleteView(DeleteView):

	model = Character
	template_name = 'characters/delete_character.html'

	def get_success_url(self):
		return reverse('characters:index')
