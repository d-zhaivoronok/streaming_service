# Generated by Django 4.2.3 on 2023-07-18 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootisfi', '0005_alter_playlist_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='image',
            field=models.ImageField(default='album_images/background_playlist.jpg', upload_to='playlist_images/'),
        ),
    ]
