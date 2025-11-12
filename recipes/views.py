# recipes/views.py
from django.http import HttpResponse


def recipe_list(request):
    return HttpResponse("レシピ一覧ページ（仮）です！")
