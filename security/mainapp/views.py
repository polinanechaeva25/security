from django.contrib.auth.models import User
from django.views.generic import ListView, View


class MainListView(ListView):
    model = User
    template_name = 'mainapp/index.html'


class CertificateListView(ListView):
    model = User
    template_name = 'mainapp/certificate.html'


class ContactListView(ListView):
    model = User
    template_name = 'mainapp/contact.html'
