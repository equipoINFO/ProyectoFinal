from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView


from .forms import SignUpForm

class Login(auth_views.LoginView):

    template_name = 'login.html'

class Logout(LoginRequiredMixin, auth_views.LogoutView):

    template_name = 'logout.html'


class SignUpView(FormView):

    template_name = 'registration/register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('apps.usuario:registercomplete')

    def form_valid(self, form):

        form.save()
        return super().form_valid(form)
        
