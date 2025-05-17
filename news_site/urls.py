from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', include('apps.news.urls')),  
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)     
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)    #Подключение статики