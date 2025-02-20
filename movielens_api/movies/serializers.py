from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Movie,Rating,Tag
from django.db.models import Avg

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','username','email','password']

    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        return user
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class MovieSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField() 
    average_rating = serializers.SerializerMethodField() 
    class Meta:
        model=Movie
        fields=['movie_id','title','genres','tags','average_rating']

    def get_tags(self,obj):
        return ','.join(obj.tag_set.values_list('tags',flat=True))
    
    def get_average_rating(self,obj):
        avg_rating=obj.rating_set.aggregate(avg=Avg('rating'))['avg']
        return round(avg_rating,2) if avg_rating else 0.0



class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields='__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'
