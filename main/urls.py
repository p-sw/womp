from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("count", views.count_womp, name="count_womp"),
    path("total", views.len_womp_file, name="len_womp_file"),
]
