from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    UserRegisterViewSet, 
    UserLoginViewSet, 
    MovieViewSet, 
    RatingViewSet, 
    TagViewSet,
    LogoutView
)

# Using DRF's router for ViewSets
router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'ratings', RatingViewSet, basename='rating')
router.register(r'tags', TagViewSet, basename='tag')

urlpatterns = [
    # User authentication URLs (separate because they use generics)
    path('register/', UserRegisterViewSet.as_view(), name='register'),
    path('login/', UserLoginViewSet.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    #  JWT Authentication Endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login & get JWT tokens
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT token

    # Include ViewSet routes
    path('', include(router.urls)),
]
