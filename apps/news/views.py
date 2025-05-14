from django.shortcuts import render
from .models import Article, Category

def homepage(request):
    articles = Article.objects.all()
    sliders = Article.objects.all()[:3]
    category = Category.objects.all()[:8]
    context = {                         #передача данные через контекст
        'articles': articles,
        'sliders': sliders,
        'category': category,
        }
    return render(request, 'index.html', context)   # Передача данных из админки в шаблон
