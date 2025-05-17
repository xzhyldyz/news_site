from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from apps.news.forms import SearchForm
from .models import Article, Category
from apps.weather.views import get_weather
from datetime import datetime
from django.utils import timezone



def search_results(request):
    categories_menu = Category.objects.all()
    form = SearchForm()
    query = ''
    news = []
    categories_r = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            news = Article.objects.filter(
                Q(title__icontains=query)  |
                Q(category__name__icontains=query)
            )
            categories_r = Category.objects.filter(
                Q(name__icontains=query)
            )
    context = {
        'form': form,
        'query': query,
        'news': news,
        'categories_menu': categories_menu,
        'categories_r': categories_r,
    }
    return render(request, 'pages/search_results.html', context)

 
def homepage(request):
    articles = Article.objects.all()
    sliders = Article.objects.all()[:3]
    categories_menu = Category.objects.all()
    weather_data = get_weather()
    current_time = datetime.now()
    context = {                       
        'articles': articles,
        'sliders': sliders,
        'categories_menu': categories_menu,
        'weather': weather_data,
        'current_time': current_time,
        }
    return render(request, 'index.html', context)


def news_detail(request, slug):
    categories_menu = Category.objects.all()
    news = get_object_or_404(Article, slug=slug)
    context = {
        'categories_menu': categories_menu,
        'news': news,
    }
    return render(request, 'details/news-detail.html', context)


def news_category(request, slug):
    categories_menu = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)
    article = Article.objects.filter(category=category)
    context = {
        'categories_menu': categories_menu,
        'article': article,
        'category': category,
    }
    return render(request, 'pages/news-category.html', context)


def contact(request):
    categories_menu = Category.objects.all()
    return render(request, 'pages/contact.html', {'categories_menu': categories_menu,})


