from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CreatePlaylist(ModelForm):
    class Meta:
        model = Playlist
        fields = ['name', 'is_public']

class CreateAlbum(ModelForm):
    class Meta:
        model = Album
        fields = ['image', 'name', 'description']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class ChangeUserForm(ModelForm):
    class Meta:
        model = Participiant
        fields = ["avatar", "name", "user_type"]

class NewSong(ModelForm):
    class Meta:
        model = Song
        fields = ["name", "lyrics", "source", "album", "genres"]