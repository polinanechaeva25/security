from django.urls import path
from mainapp.views import MainListView, CertificateListView, ContactListView

app_name = 'mainapp'

urlpatterns = [
    path('', MainListView.as_view(), name='index'),
    path('certificate/', CertificateListView.as_view(), name='certificate'),
    path('contact/', ContactListView.as_view(), name='contact'),
]