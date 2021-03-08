# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField('nombre', max_length=60)
    mail = models.CharField('mail', max_length=60)
    asunto = models.CharField('asunto', max_length=100)
    comentario = models.TextField()


class Materias(models.Model):
    id_materia = models.AutoField(primary_key=True)
    nombre =  models.CharField('nombre', max_length=20)

class Profesor(models.Model):
    id_profesor = models.AutoField(primary_key=True)
    nombre = models.CharField('nombre', max_length=30)





"""
class VerTurno(models.Model):
    id_turno =  models.IntegerField()
    nombre =  models.CharField('nombre', max_length=20)


class Clase(models.Model):
    id_clase = ForeignKey(id_clase, null=false, blank=false, on_delete=models.CASCADE)
    id_materia = models.IntegerField()
    id_profesor = models.IntegerField()
    modalidad = models.CharField('modalidad', max_length=20)
    horario = models.DataTime()

class ClaseReserva(models.Model):
    id_clase = models.IntegerField()
    id_alumno = models.IntegerField()
    fe_incripsion = models.DateField.auto_now()

class Materia(models.Model):
    id_materia =  models.IntegerField()
    nombre = models.CharField('nombre', max_length=60)


class Profesor(models.Model):
    id_profesor = models.IntegerField()
    nombre = models.CharField('nombre', max_length=60)
    correo = models.CharField('nombre', max_length=60)
    celular = models.CharField('celular', max_length=20)
"""
