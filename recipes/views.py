from django.shortcuts import get_object_or_404, render
from recipes.models import Recipe
from blogs.models import Blog
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def recipe_ru(request):
    recipes = Recipe.objects.order_by('-created_date')
    recent_blogs_ru   = Blog.objects.order_by('-created_date')[:4]
    paginator = Paginator(recipes, 10)
    page = request.GET.get('page')
    paged_recipes = paginator.get_page(page)
    
    data = {
        'recipes': paged_recipes,
        'recent_blogs_ru':    recent_blogs_ru,
    }
    
    return render(request, 'recipes/recipes_ru.html', data)

def recipe_az(request):
    recipes = Recipe.objects.order_by('-created_date')
    recent_blogs_az   = Blog.objects.order_by('-created_date')[:4]
    paginator = Paginator(recipes, 10)
    page = request.GET.get('page')
    paged_recipes = paginator.get_page(page)
    
    data = {
        'recipes': paged_recipes,
        'recent_blogs_az':    recent_blogs_az,
    }
    
    return render(request, 'recipes/recipes_az.html', data)

def single_recipe_ru(request, id):
    single_recipe    = get_object_or_404(Recipe, pk=id)
    recent_blogs_ru   = Blog.objects.order_by('-created_date')[:4]
    
    data = {
        'single_recipe': single_recipe,
        'recent_blogs_ru':    recent_blogs_ru,
    }
    
    return render(request, 'recipes/single_recipe_ru.html', data)

def single_recipe_az(request, id):
    single_recipe    = get_object_or_404(Recipe, pk=id)
    recent_blogs_az   = Blog.objects.order_by('-created_date')[:4]
    
    data = {
        'single_recipe': single_recipe,
        'recent_blogs_az':    recent_blogs_az,
    }
    
    return render(request, 'recipes/single_recipe_az.html', data)

def search_ru(request):
    recipes = Recipe.objects.order_by('-created_date')
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            recipes = recipes.filter(Q(recipe_title_ru__icontains=keyword) | Q(recipe_description_ru__icontains=keyword))
            
    data = {
        'recipes':  recipes,
    }
    
    return render(request, 'recipes/recipes_ru.html', data)

def search_az(request):
    recipes = Recipe.objects.order_by('-created_date')
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            recipes = recipes.filter(Q(recipe_title_az__icontains=keyword) | Q(recipe_description_az__icontains=keyword))
            
    data = {
        'recipes':  recipes,
    }
    
    return render(request, 'recipes/recipes_az.html', data)