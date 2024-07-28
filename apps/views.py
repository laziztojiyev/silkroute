from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from apps.models import Packages


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ServicesView(TemplateView):
    template_name = 'service.html'


class PackagesView(ListView):
    template_name = 'blog.html'
    model = Packages
    context_object_name = 'packages'


class PackageDetailView(DetailView):
    template_name = 'single.html'
    model = Packages
    context_object_name = 'package'


class ContactView(TemplateView):
    template_name = 'contact.html'
