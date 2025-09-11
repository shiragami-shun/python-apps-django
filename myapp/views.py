# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("やーい、ひっかかったなばーか(・ω<)")


def html(request):
    context = {"key": "value"}
    return render(request, "profile_shiragami_shun/index.html", context)

