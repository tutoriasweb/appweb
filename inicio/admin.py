# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Contacto, Materias, Profesor

# Register your models here.
admin.site.register(Contacto)
admin.site.register(Materias)
admin.site.register(Profesor)
