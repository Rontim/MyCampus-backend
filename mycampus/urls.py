from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('api/v1/user/', include('user.urls')),
    path('api/v2/', include('djoser.urls')),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
