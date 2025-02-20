from rest_framework import viewsets, mixins,permissions
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.exceptions import ValidationError
from rest_framework import generics,status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Movie, Rating, Tag
from .serializers import MovieSerializer, RatingSerializer, TagSerializer,UserRegisterSerializer,UserLoginSerializer

# Create your views here.

class UserRegisterViewSet(generics.CreateAPIView):
     queryset=User.objects.all()
     serializer_class=UserRegisterSerializer


class UserLoginViewSet(APIView):
    @swagger_auto_schema(
        request_body=UserLoginSerializer,  # Explicitly tell Swagger about input fields
        responses={200: "Login Successful", 401: "Invalid credentials"}
    )
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh)
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")  # Get refresh token from request
            token = RefreshToken(refresh_token)
            token.blacklist()  # Blacklist the token
            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
    

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    #  Enables filtering & ordering
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]  
    ordering_fields = ['title']  #  Allows ordering by title

    #  Filtering by genres and tags (modify if genres is ManyToManyField)
    filterset_fields = {
    'genres': ['icontains'],  
    'tag__tags': ['icontains']  # ✅ Correct field for ForeignKey (not tag_set__tags)
}


class RatingViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        movie = serializer.validated_data['movie']

        if Rating.objects.filter(user=user, movie=movie).exists():
            raise ValidationError('You have already rated this movie.')
        serializer.save(user=user)


class TagViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]
