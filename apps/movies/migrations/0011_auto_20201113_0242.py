# Generated by Django 3.0.5 on 2020-11-12 23:42

from django.db import migrations, models
import movies.models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_film_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='video',
            field=models.FileField(null=True, upload_to=movies.models.get_film_path),
        ),
    ]
