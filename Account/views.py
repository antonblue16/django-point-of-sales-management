from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from . import forms

# Create your views here.

class Register(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/register.html'

class Login(LoginView):
    template_name = 'accounts/login.html'