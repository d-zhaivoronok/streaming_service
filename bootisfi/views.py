from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import random

from .models import *
from .forms import *

# Create your views here.

def signupUser(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Participiant.objects.create(user=user, name=user.username, user_type='user')
            return redirect('login')

    context = {'form': form}
    return render(request, "bootisfi/signup.html", context=context)

def home(request):
    new_albums = Album.objects.all().order_by("-time_of_posting")[:5]
    top_charts = Song.objects.all().order_by("-views_counter")[:12]

    context = {'new_albums': new_albums, 'top_charts': top_charts}

    if request.user.is_authenticated:
        user = request.user
        recently_listened_songs = SongListening.objects.all().filter(user=request.user).order_by("-listened_at")[:12]
        context['recently_listened_songs_count'] = recently_listened_songs.count()
        context['recently_listened_songs'] = recently_listened_songs[:5]

        recently_listened_songs_genres_count = {}

        for song in recently_listened_songs:
            genre_name = song.song.genres.values()[0]['name']
            recently_listened_songs_genres_count[genre_name] = recently_listened_songs_genres_count.get(genre_name,
                                                                                                        0) + 1

        recommended_songs = []

        for genre, count in recently_listened_songs_genres_count.items():
            songs_with_genre = Song.objects.filter(genres__name=genre)
            random_songs = random.sample(list(songs_with_genre), min(count, len(songs_with_genre)))
            recommended_songs.extend(random_songs)

        random.shuffle(recommended_songs)

        context['recommendation'] = recommended_songs[:12]

    return render(request, "bootisfi/index.html", context=context)


def listen(request, song_id):
    song = Song.objects.get(id=song_id)
    song.views_counter += 1
    song.save()

    SongListening.objects.create(user=request.user, song=song)

    new_albums = Album.objects.all().order_by("-time_of_posting")[:5]
    top_charts = Song.objects.all().order_by("-views_counter")[:12]
    context = {'song': song, 'new_albums': new_albums, 'top_charts': top_charts}
    if request.user.is_authenticated:
        user = request.user

        recently_listened_songs = SongListening.objects.all().filter(user=request.user).order_by("-listened_at")
        context['recently_listened_songs_count'] = recently_listened_songs.count()
        context['recently_listened_songs'] = recently_listened_songs[:5]

        recently_listened_songs_genres_count = {}

        for song in recently_listened_songs:
            genre_name = song.song.genres.values()[0]['name']
            recently_listened_songs_genres_count[genre_name] = recently_listened_songs_genres_count.get(genre_name,
                                                                                                        0) + 1

        recommended_songs = []

        for genre, count in recently_listened_songs_genres_count.items():
            songs_with_genre = Song.objects.filter(genres__name=genre)
            random_songs = random.sample(list(songs_with_genre), min(count, len(songs_with_genre)))
            recommended_songs.extend(random_songs)

        random.shuffle(recommended_songs)

        context['play_next'] = recommended_songs

        context['recommendation'] = recommended_songs[:12]
    return render(request, "bootisfi/play_song.html", context=context)

@login_required(login_url='login')
def library(request):
    if request.method == 'POST':
        form = CreatePlaylist(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.user_or_band = request.user
            playlist.save()
            return redirect('library')
    else:
        form = CreatePlaylist()

    context = {'form': form}
    library = Playlist.objects.all().filter(user_or_band=request.user)
    if request.user.participiant.user_type == 'band':
        albums = Album.objects.all().filter(user_or_band=request.user)
        context['albums'] = albums
    context['library'] = library
    return render(request, "bootisfi/library.html", context=context)

@login_required(login_url='login')
def library_filters(request, filter):
    if filter == "playlists":
        library = Playlist.objects.all().filter(user_or_band=request.user)
        context = {"library": library}
    elif filter == "albums":
        albums = Album.objects.all().filter(user_or_band=request.user)
        context = {'albums': albums}

    return render(request, "bootisfi/library.html", context=context)

@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        form = ChangeUserForm(request.POST, request.FILES, instance=request.user.participiant)
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            return redirect('profile')
    else:
        form = ChangeUserForm()

    context = {'form': form}
    return render(request, "bootisfi/profile.html", context=context)

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    context = {}
    return render(request, "bootisfi/login.html", context=context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect("home")