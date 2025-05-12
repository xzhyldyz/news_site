from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
    

class Article(models.Model):
    title = models.CharField(max_length=255)  #Заголовок статьи
    content = models.TextField()  #Основной тект статьи
    published_date = models.DateTimeField(auto_now_add=True) #Дата публикации
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='articles') #Категория
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  #Автор статьи
    image = models.ImageField(upload_to='articles/', null=True, blank=True) #Изображение
    views = models.PositiveIntegerField(default=0)  #Кол-во просмотров
    comments_count = models.PositiveIntegerField(default=0)  #Кол-во комментариев

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title
    

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Коммент"
        verbose_name_plural = "Коментарии"

    def __str__(self):
        return f"Comment by {self.author} on {self.article.title}"


class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    condition = models.CharField(max_length=50)

    def __str__(self):
        return self.city
    
class Kursy_valyut(models.Model):
    valuta = models.CharField(max_length=100)
    kursy = models.FloatField()

    def __str__(self):
        return f"{self.valuta} - {self.kursy}"





    


    


