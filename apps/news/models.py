from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})
    

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"
    

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст")
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, 
        related_name='articles', verbose_name="Категория"
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, 
        null=True, blank=True, verbose_name="Автор"
    )
    image = models.ImageField(
        upload_to='articles/', 
        null=True, blank=True, verbose_name="Фото"
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Новости - cтатья"
        verbose_name_plural = "Новости - Статьи"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments'
    )
    author = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "коммент"
        verbose_name_plural = "Коментарии"

    def __str__(self):
        return f"Автор: {self.author} к {self.article.title}"
    