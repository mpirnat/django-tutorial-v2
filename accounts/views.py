from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

from accounts.forms import RegistrationForm


class RegistrationView(FormView):

    template_name = 'registration/register.html'
    form_class = RegistrationForm

    def form_valid(self, form):
        form.save()

        user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'])
        login(self.request, user)

        return super(RegistrationView, self).form_valid(form)

    def get_success_url(self):
        return reverse('characters:index')

