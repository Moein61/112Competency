from django.contrib import admin
from .models import Genre, Movie

#create Admin template for the models
class GenreAdmin(admin.ModelAdmin):
    list_dispalay = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
    list_dispaly_links = ('id', 'title')
    list_display = ('id', 'title', 'release_year', 'price', 'in_stock')
    #exclude = ('in_stock', 'price')
    #fields = ('title', 'genre', 'in_4k')

# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)