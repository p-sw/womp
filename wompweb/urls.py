from django.urls import path, include
from django.views.generic impor TemplateView

urlpatterns = [
    path('', include('main.urls', namespace='main')),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml')),
]
