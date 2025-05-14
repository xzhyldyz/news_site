from django.shortcuts import render
from .models import Article, Category

def homepage(request):
    articles = Article.objects.all()
    sliders = Article.objects.all()[:3]
    category = Category.objects.all()
    context = {                       
        'articles': articles,
        'sliders': sliders,
        'category': category,
        }
    return render(request, 'index.html', context)   # Передача данных из админки в шаблон

def sport_category(request):
    sport_category = Category.objects.get(name = 'спорт')
    articles = Article.objects.filter(category=sport_category)
    
    return render(request, 'pages/news-category-sport.html', {'articles': articles})

