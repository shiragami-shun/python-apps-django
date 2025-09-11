# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def top(request):
    return HttpResponse("バカ丸出しですねw")


def index(request):
    return HttpResponse("やーい、ひっかかったなばーか(・ω<)")


def html(request):
    context = {"key": "value"}
    return render(request, "profile_shiragami_shun/index.html", context)
