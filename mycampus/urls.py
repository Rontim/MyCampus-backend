from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="MyCampus API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('api/v1/user/', include('user.urls')),
    path('api/v1/interaction/', include('interactions.urls')),
    path('api/v2/', include('djoser.urls')),
    path('api/v1/club/', include('club.urls')),
    path('api/v1/topic/', include('topic.urls')),
    path('api/v1/image/', include('images.urls')),
    path('api/v1/blog/', include('blog.urls')),
    path('api/v1/likes/', include('likes.urls')),
    path('api/v1/comment/', include('comments.urls')),
    path('api/v1/', include('api.urls')),

] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
