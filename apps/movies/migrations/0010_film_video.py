# Generated by Django 3.0.5 on 2020-11-12 23:41

from django.db import migrations, models
import movies.models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_auto_20201113_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='video',
            field=models.FileField(null=True, upload_to=movies.models.get_trailer_path),
        ),
    ]
