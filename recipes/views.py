# recipes/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm


def recipe_list(request):
    """レシピ一覧ページ"""
    recipes = Recipe.objects.all().order_by('-created_at')
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


def recipe_detail(request, pk):
    """レシピ詳細ページ"""
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


def recipe_create(request):
    """レシピ新規作成"""
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {
        'form': form, 'title': '新しいレシピを追加'
        })


def recipe_edit(request, pk):
    """レシピ編集"""
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_form.html', {
        'form': form, 'title': 'レシピを編集'
        })


def recipe_delete(request, pk):
    """レシピ削除"""
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'recipes/recipe_delete.html', {'recipe': recipe})
