import requests
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from apps.news.forms import SearchForm
from .models import Article, Category, SocialLink
from apps.weather.views import get_weather

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
                Q(title__icontains=query) |
                Q(content__icontains=query) |
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

def get_city_time():
    try:
        response = requests.get('https://timeapi.io/api/Time/current/zone?timeZone=Asia/Bishkek')
        data = response.json()
        datetime_str = data.get('dateTime')  # формат: '2025-05-18T18:30:15'

        if datetime_str:
            dt = datetime.fromisoformat(datetime_str)
            return dt.strftime('%d.%m.%Y %H:%M')  # формат: 18.05.2025 18:30
    except Exception as e:
        print(f"Ошибка при получении времени: {e}")
        return "❗ Время недоступно"


 
def homepage(request):  
    articles = Article.objects.all()
    sliders = Article.objects.all()[:3]
    categories_menu = Category.objects.all()
    weather_data = get_weather()
    city_time = get_city_time()
    social_links = SocialLink.objects.first()
    context = {                       
        'articles': articles,   
        'sliders': sliders,
        'categories_menu': categories_menu,
        'weather': weather_data,
        'city_time': city_time,
        'social_links': social_links,
        }
    return render(request, 'index.html', context)   # Передача данных из админки в шаблон

def breaking_news(request):
    breaking_articles = Article.objects.filter(is_breaking=True)
    return render(request, 'pages/breaking_news.html',{
        'breaking_articles': breaking_articles
    })



def news_detail(request, slug):
    categories_menu = Category.objects.all()
    news = get_object_or_404(Article, slug=slug)
    context = {
        'categories_menu': categories_menu,
        'news': news,
    }
    return render(request, 'details/news_detail.html', context)


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


