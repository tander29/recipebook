from django.shortcuts import render, get_object_or_404
from .models import Recipe, Author, User
from .forms import AddAuthor, AddRecipe


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


def add_author(request):
    html_get = 'addauthor.html'
    if request.method == 'POST':
        form = AddAuthor(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['name']
            )
            Author.objects.create(
                name=data['name'],
                user=user,
                bio=data['bio']
            )
            return render(request, 'confirmation.html', {'record': 'Author'})
    else:
        form = AddAuthor()
        return render(request, html_get, {'form': form})


def add_recipe(request):
    html_template = 'addrecipe.html'
    if request.method == 'POST':
        form = AddRecipe(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                time=data['time'],
                instructions=data['instructions']
            )
            return render(request, 'confirmation.html', {'record': 'Recipe!'})
    else:
        form = AddRecipe()
        return render(request, html_template, {'form': form})
