# Generated by Django 4.2.3 on 2023-07-18 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootisfi', '0007_alter_playlist_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='is_public',
            field=models.CharField(choices=[('public', 'Публічний'), ('private', 'Приватний')], default='public', max_length=7),
        ),
    ]
