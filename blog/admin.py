from django.contrib import admin
from .models import Post, MovieDirector, MovieDetails

# Register your models here.

admin.site.register(Post)
admin.site.register(MovieDirector)
admin.site.register(MovieDetails)