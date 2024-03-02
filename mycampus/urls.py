from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('api/v1/user/', include('user.urls')),
    path('api/v1/interaction/', include('interactions.urls')),
    path('api/v2/', include('djoser.urls')),
    path('api/v1/club/', include('club.urls')),
    path('api/v1/topic/', include('topic.urls')),
    path('api/v1/image/', include('images.urls')),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
