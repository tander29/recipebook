from django.shortcuts import render, get_object_or_404
from .models import Recipe, Author


def index(request):
    return render(request, 'index.html', {'recipes': Recipe.objects.all()})


def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    author = get_object_or_404(Author, pk=recipe.author.id)
    return render(request, 'recipe.html',
                  {'recipe': recipe, 'author': author})


def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    recipes = Recipe.objects.filter(author_id=author_id)
    return render(request, 'author.html',
                  {'author': author, 'recipes': recipes})
