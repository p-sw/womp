from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('main.urls', namespace='main')),
]
