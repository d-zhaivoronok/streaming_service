import uuid

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Participiant(models.Model):
    # Choices for the band/user select field
    USER_TYPE_CHOICES = (
        ('user', 'User'),
        ('band', 'Band'),
    )

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True, unique=True)
    user_type = models.CharField(max_length=4, choices=USER_TYPE_CHOICES, default='user')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, default='avatars/avatar.jpg')


class SongListening(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey('Song', on_delete=models.CASCADE)
    listened_at = models.DateTimeField(auto_now_add=True)
class Song(models.Model):
    # Fields for the Song model
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    lyrics = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.FileField(upload_to='audio/', null=True, blank=True)
    album = models.ForeignKey('Album', on_delete=models.CASCADE, blank=True, null=True)
    views_counter = models.PositiveIntegerField(default=0)
    genres = models.ForeignKey('Genre', on_delete=models.CASCADE, blank=True, null=True)
    time_of_posting = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
class Album(models.Model):
    # Fields for the Album model
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='album_images/')
    description = models.CharField(max_length=1000, null=True, blank=True)
    user_or_band = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    time_of_posting = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Playlist(models.Model):
    PLAYLIST_TYPE_CHOICES = (
        ('public', 'Публічний'),
        ('private', 'Приватний'),
    )
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='playlist_images/', default="playlist_images/background_palylist.jpg")
    user_or_band = models.ForeignKey(User, on_delete=models.CASCADE)
    time_of_posting = models.DateTimeField(auto_now_add=True)
    is_public = models.CharField(max_length=7, choices=PLAYLIST_TYPE_CHOICES, default='public')
    songs = models.ManyToManyField('Song', blank=True)