from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.conf import settings
from django.conf.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/jwt/create', TokenObtainPairView.as_view()),
    path('api/v1/jwt/refresh', TokenRefreshView.as_view()),
    path('api/v1/jwt/verify', TokenVerifyView.as_view()),
    path('api/v1/user/', include('user.urls')),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
