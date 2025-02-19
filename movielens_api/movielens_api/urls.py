from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# ✅ Swagger Schema View
schema_view = get_schema_view(
    openapi.Info(
        title="MovieLens API",
        default_version="v1",
        description="API documentation for MovieLens dataset application",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="admin@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),  # ✅ Django Admin
    path("api/", include("movies.urls")),  # ✅ Include your app's URLs
    
    # ✅ Swagger & ReDoc at the project level
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
