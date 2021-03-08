# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views.generic import TemplateView
from inicio.models import Contacto, Materias, Profesor

"""
def user_login(TemplateView):
    def get(self, request, **kwargs):
        if request.method == 'POST':
            # extrae los datos
            username = request.POST['username']
            password = request.POST['password']
            # Check username and password combination if correct
            user = authenticate(username=username, password=password)
            if user is not None:
                # Graba en la Cooking
                login(request, user)
                # Proceso Correcto
                return render(request, 'about.html')
            else:
                # Incorrect credentials, let's throw an error to the screen.
                return render(request, 'login.html', {'error_message': 'Incorrect username and / or password.'})
        else:
            # Muestra el login al iniciar
            return render(request, 'login.html')
"""

class ReservarView(TemplateView):
    def get(self, request, **kwargs):
        materias = Materias.objects.all()
        profesores = Profesor.objects.all()
        return render(request, 'reserva.html', {'Materias': materias, 'Profesores': profesores})



class HomePageView(TemplateView):
    template_name = "index.html"



class ContactoView(TemplateView):
    def get(self, request, **kwargs):
        contacto = Contacto.objects.all()
        return render(request, 'vercontacto.html', {'contactos': contacto})


class AboutPageView(TemplateView):
    template_name = "about.html"

class DataPageView(TemplateView):
    def get(self, request, **kwargs):
        # we will pass this context object into the
        # template so that we can access the data
        # list in the template
        context = {
            'data': [
                { 'name': 'Celeb 1', 'worth': '3567892' },
                { 'name': 'Celeb 2', 'worth': '23000000'},
                { 'name': 'Celeb 3', 'worth': '1000007' },
                { 'name': 'Celeb 4', 'worth': '456789'  },
                { 'name': 'Celeb 5', 'worth': '7890000' },
                { 'name': 'Celeb 6', 'worth': '12000456'},
                { 'name': 'Celeb 7', 'worth': '896000'  },
                { 'name': 'Celeb 8', 'worth': '670000'  }
            ]
        }
        return render(request, 'data.html', context)
