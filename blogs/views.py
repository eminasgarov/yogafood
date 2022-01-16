from django.shortcuts import get_object_or_404, render
from blogs.models import Blog
from recipes.models import Recipe
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def blog_ru(request):
    recent_recipes_ru   = Recipe.objects.order_by('-created_date')[:4]
    blogs = Blog.objects.order_by('-created_date')
    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)
    
    data = {
        'recent_recipes_ru':    recent_recipes_ru,
        'blogs':                paged_blogs,
    }
    return render(request, 'blogs/blogs_ru.html', data)

def blog_az(request):
    recent_recipes_az   = Recipe.objects.order_by('-created_date')[:4]
    blogs = Blog.objects.order_by('-created_date')
    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)
    
    data = {
        'recent_recipes_az':    recent_recipes_az,
        'blogs':                paged_blogs,
    }
    return render(request, 'blogs/blogs_az.html', data)

def single_blog_ru(request, id):
    recent_recipes_ru   = Recipe.objects.order_by('-created_date')[:4]
    single_blog    = get_object_or_404(Blog, pk=id)
    data = {
        'recent_recipes_ru':    recent_recipes_ru,
        'single_blog': single_blog,
    }
    
    return render(request, 'blogs/single_blog_ru.html', data)

def single_blog_az(request, id):
    recent_recipes_az   = Recipe.objects.order_by('-created_date')[:4]
    single_blog    = get_object_or_404(Blog, pk=id)
    data = {
        'recent_recipes_az':    recent_recipes_az,
        'single_blog': single_blog,
    }
    
    return render(request, 'blogs/single_blog_az.html', data)

def search_ru(request):
    blogs = Blog.objects.order_by('-created_date')
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            blogs = blogs.filter(Q(blog_title_ru__icontains=keyword) | Q(blog_description_ru__icontains=keyword))
            
    data = {
        'blogs':  blogs,
    }
    
    return render(request, 'blogs/blogs_ru.html', data)

def search_az(request):
    blogs = Blog.objects.order_by('-created_date')
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            blogs = blogs.filter(Q(blog_title_az__icontains=keyword) | Q(blog_description_az__icontains=keyword))
            
    data = {
        'blogs':  blogs,
    }
    
    return render(request, 'blogs/blogs_az.html', data)