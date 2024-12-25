from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Project Management API",
        default_version='v1',
        description="API documentation for the Project Management tool",
    ),
    public=True,
)

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Swagger documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # API routes
    path('api/', include('api.urls')),  # Include the API routes from api/urls.py
]
