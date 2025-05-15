from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
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


def news_detail(request, slug):
    category = Category.objects.all()
    news = get_object_or_404(Article, slug=slug)
    context = {
        'category': category,
        'news': news,
    }
    return render(request, 'details/news-detail.html', context)


def contact(request):
    category = Category.objects.all()
    return render(request, 'pages/contact.html', {'category': category,})

