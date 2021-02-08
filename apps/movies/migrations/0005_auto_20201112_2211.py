# Generated by Django 3.0.5 on 2020-11-12 19:11

from django.db import migrations, models
import movies.models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20201112_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to=movies.models.get_poster_path, verbose_name='Poster'),
        ),
        migrations.AlterField(
            model_name='movieshots',
            name='image',
            field=models.ImageField(upload_to=movies.models.get_shots_path, verbose_name='Image'),
        ),
    ]
