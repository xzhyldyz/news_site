from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Article, Category
 
def homepage(request):
    articles = Article.objects.all()
    sliders = Article.objects.all()[:3]
    categories = Category.objects.all()
    context = {                       
        'articles': articles,
        'sliders': sliders,
        'categories': categories,
        }
    return render(request, 'index.html', context)   # Передача данных из админки в шаблон


def news_detail(request, slug):
    categories = Category.objects.all()
    news = get_object_or_404(Article, slug=slug)
    context = {
        'categories': categories,
        'news': news,
    }
    return render(request, 'details/news-detail.html', context)


def news_category(request, slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)
    article = Article.objects.filter(category=category)
    context = {
        'categories': categories,
        'article': article,
        'category': category,
    }
    return render(request, 'pages/news-category.html', context)


def contact(request):
    categories = Category.objects.all()
    return render(request, 'pages/contact.html', {'categories': categories,})

