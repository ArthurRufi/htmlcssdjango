from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_publish = True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        'is_detail_page':False,
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipes': Recipe.objects.filter(pk=id, is_publish = True).order_by('-id'),
        'is_detail_page': True
        

    })


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id = category_id, is_publish = True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        'is_detail_page':True,
    })
