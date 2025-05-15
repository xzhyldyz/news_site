from django.urls import path
from apps.news import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('category/<slug:slug>/', views.news_category, name='news_category'),
    path('contact/', views.contact, name="contactPages"),
]   