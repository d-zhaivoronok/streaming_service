from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Participiant)
class ParticipiantAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_type', 'avatar')  # Customize which fields to display in the list view
    list_filter = ('user_type',)  # Add filters on user_type in the right sidebar
    search_fields = ('username',)  # Add a search ba

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'album', 'time_of_posting')
    list_filter = ('author', 'album', 'time_of_posting')
    search_fields = ('name', 'author__username', 'album__name')

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_or_band', 'time_of_posting')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Album)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_of_posting')

@admin.register(SongListening)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('user', 'song', 'listened_at',)