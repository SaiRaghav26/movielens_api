import csv
from django.core.management.base import BaseCommand
from movies.models import Movie,Rating,Tag

from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help='Load 20M Movielens dataset'

    def handle(self,*args,**kwargs):
        self.load_movies()
        self.load_tags()
        self.stdout.write(self.style.SUCCESS('Successfully loaded dataset'))

    def load_movies(self):
        with open(r'C:\Users\Analog\Desktop\amro assignment\assignment 2\movielens data set\ml-20m\movies.csv',newline='',encoding='utf-8') as file:
            reader=csv.reader(file)
            next(reader)
            Movie.objects.bulk_create(
                [
                    Movie(movie_id=row[0],title=row[1],genres=row[2])
                    for row in reader
                ]
            )

    def load_tags(self):
        User=get_user_model()
        with open(r'C:\Users\Analog\Desktop\amro assignment\assignment 2\movielens data set\ml-20m\tags.csv',newline='',encoding='utf-8') as file:
            reader=csv.reader(file)
            next(reader)

            tags=[]
            for row in reader:
                user_id=row[0]
                movie_id=row[1]
                tag_text=row[2]
                timestamp=row[3]

                #try to fetch user if not found,set user to None
                user=User.objects.filter(id=user_id).first()

                #fetch movie
                try:
                    movie=Movie.objects.get(movie_id=movie_id)
                except Movie.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Movie {movie_id} not found. Skipping."))
                    continue  # Skip this tag if the movie does not exist

                #append tag instance
                tags.append(Tag(user=user,movie=movie,tags=tag_text,timestamp=timestamp))
        Tag.objects.bulk_create(tags)  # Efficient bulk insert
        self.stdout.write(self.style.SUCCESS(f"{len(tags)} tags inserted successfully."))


