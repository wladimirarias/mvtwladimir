from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app.models import Familia

# Create your views here.

def lista_familia (request):
    familiares = Familia.objects.all()

    datos = {
        "familiares": familiares,
    }

    plantilla = loader.get_template("template.html")

    documento = plantilla.render(datos)
    return HttpResponse(documento)