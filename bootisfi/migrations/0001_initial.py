# Generated by Django 4.2.3 on 2023-07-19 01:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='album_images/')),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('name', models.CharField(max_length=100)),
                ('time_of_posting', models.DateTimeField(auto_now_add=True)),
                ('user_or_band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('lyrics', models.TextField()),
                ('source', models.FileField(blank=True, null=True, upload_to='audio/')),
                ('views_counter', models.PositiveIntegerField(default=0)),
                ('time_of_posting', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bootisfi.album')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('genres', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='bootisfi.genre')),
            ],
        ),
        migrations.CreateModel(
            name='SongListening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listened_at', models.DateTimeField(auto_now_add=True)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bootisfi.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(default='playlist_images/background_palylist.jpg', upload_to='playlist_images/')),
                ('time_of_posting', models.DateTimeField(auto_now_add=True)),
                ('is_public', models.CharField(choices=[('public', 'Публічний'), ('private', 'Приватний')], default='public', max_length=7)),
                ('songs', models.ManyToManyField(blank=True, to='bootisfi.song')),
                ('user_or_band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Participiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('user_type', models.CharField(choices=[('user', 'User'), ('band', 'Band')], default='user', max_length=4)),
                ('avatar', models.ImageField(blank=True, default='avatars/avatar.jpg', null=True, upload_to='avatars/')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
