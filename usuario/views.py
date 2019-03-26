from django.shortcuts import render

from django.views.generic import TemplateView

#reate your views here.
class IndexView(TemplateView):
    template_name = "index.html"

#Como funcionam as classes dentro do “views”:
class UsuarioModuloView(TemplateView):
    template_name = "inicio.html"
