from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.recipes.factory import make_recipe
from recipes.models import Recipe


def home(request):
    recipes = get_list_or_404( 
        Recipe.objects.filter(
            is_publish = True,
        ).order_by('-id'))
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        'is_detail_page':False,
    })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_publish = True)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True
    })


def category(request, category_id):
    recipes = get_list_or_404( 
        Recipe.objects.filter(
            category__id = category_id,
            is_publish = True,
        ).order_by('-id'))

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'is_detail_page':True,
        'title': f'{recipes[0].category.name} - Categoty |'
    })
