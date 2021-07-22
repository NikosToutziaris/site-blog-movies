from django.db import models
from django.utils import timezone
from PIL import Image
from model_utils import Choices
from datetime import datetime


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    movie_details = models.ForeignKey('MovieDetails', null=True, on_delete=models.CASCADE)
    published_date = models.DateTimeField(blank=True, null=True)


class MovieDirector(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    SEX = Choices('male', 'female')
    sex = models.CharField(choices=SEX, max_length=20)
    NATIONALITY = Choices('American', ' Czechoslovakian', 'English', 'French', 'German', 'Greek',
                          'Italian', 'New Zealand', 'Spanish')
    nationality = models.CharField(max_length=200, choices=NATIONALITY)
    birthday = models.DateField()
    resume = models.TextField()


class MovieDetails(models.Model):
    title = models.CharField(max_length=100)
    duration = models.DurationField()  # TimeField(u"Conversation Time", blank=True)
    movie_director = models.ForeignKey('MovieDirector', null=True, on_delete=models.CASCADE)
    MOVIE_KINDS = Choices('Action', 'Comedy', 'Romantic', 'Adventure', 'Musical', 'Drama', 'Historical', 'Real life',
                          'War', 'Horror', 'Science Fiction', 'Thriller', 'Biographical', 'Feature', 'Satirical',
                          'Dystopian')
    movie_kind = models.CharField(choices=MOVIE_KINDS, max_length=200)
    LANGUAGES = Choices('English', 'French', 'German', 'Greek', 'Italian', 'Spanish')
    language = models.CharField(choices=LANGUAGES, max_length=200)
    first_screening_date = models.DateField()
    imdb_url = models.CharField(max_length=200)
    imdb_grading = models.FloatField()
    grading = models.FloatField()
    imdb_summary = models.CharField(max_length=200)
    review = models.CharField(max_length=200)
    image = models.ImageField(null=True)