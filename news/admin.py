from django.contrib import admin
from .models import Article, Category, Tag, Comment, Weather, Kursy_valyut

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Weather)
admin.site.register(Kursy_valyut)

