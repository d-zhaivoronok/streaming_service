# Generated by Django 4.2.3 on 2023-07-17 23:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bootisfi', '0003_rename_username_participiant_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
