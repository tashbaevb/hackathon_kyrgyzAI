from django.urls import path, include
from django.contrib import admin

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="KyrgyzAI",
        default_version='v1',
        description="Swagger",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ]
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/users/', include('account.urls')),
    path('course/', include('course.urls')),
    path('content/', include('content.urls')),
    path('api/v1/lessons/', include('lesson.urls')),
    path('ai/', include('tts_api.urls')),
    path('api/v1/tasks/', include('task.urls')),
    path('api/v1/tts/', include('tts_api.urls')),

    # Swagger
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
