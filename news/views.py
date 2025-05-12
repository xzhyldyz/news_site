from django.shortcuts import render
from .models import Article

def homepage(request):
    articles = Article.objects.all()
    context = {                         #передача данные через контекст
        'articles': articles
        }
    return render(request, 'index.html', context)   # Передача данных из админки в шаблон
