from django.urls import path
from apps.news import views


urlpatterns = [
    path('', views.homepage, name="home"),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('breaking', views.breaking_news, name='breaking_news'),
    path('category/<slug:slug>/', views.news_category, name='news_category'),
    path('search/', views.search_results, name='search'),
    path('contact/', views.contact, name="contactPages"),
]