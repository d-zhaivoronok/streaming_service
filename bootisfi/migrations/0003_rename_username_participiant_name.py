# Generated by Django 4.2.3 on 2023-07-17 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bootisfi', '0002_alter_playlist_songs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participiant',
            old_name='username',
            new_name='name',
        ),
    ]