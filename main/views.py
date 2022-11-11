from django.shortcuts import render
from django.http.response import JsonResponse
from django.conf import settings

import os

from .models import WompCounter

# Create your views here.


def index(request):
    if not WompCounter.objects.all():
        womps = WompCounter.objects.create(womp_count=0)
    else:
        womps = WompCounter.objects.first()
    return render(request, "index.html", {"womps": womps})


def count_womp(request):
    womps = WompCounter.objects.first()
    womps.womp_count += 1
    womps.save()
    return JsonResponse({"womps": womps.womp_count})


def len_womp_file(request):
    length_womps = len(os.listdir(os.path.join(settings.BASE_DIR, "womps")))
    return JsonResponse({"total": length_womps})
