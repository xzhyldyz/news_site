from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.news.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="home"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)     
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)    #Подключение статики