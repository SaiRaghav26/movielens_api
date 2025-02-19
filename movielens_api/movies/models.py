from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    movie_id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=255)
    genres=models.TextField(default='')


class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,related_name='rating_set',on_delete=models.CASCADE)
    rating=models.FloatField()
    timestamp=models.BigIntegerField()

    class Meta:
        unique_together=('user','movie')


class Tag(models.Model):
    user=models.ForeignKey(User,related_name='tag_set',on_delete=models.CASCADE,null=True, blank=True)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    tags=models.CharField(max_length=255)
    timestamp=models.BigIntegerField()





