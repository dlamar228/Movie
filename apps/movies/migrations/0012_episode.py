# Generated by Django 3.0.5 on 2020-11-13 00:08

from django.db import migrations, models
import django.db.models.deletion
import movies.models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_auto_20201113_0242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode', models.PositiveSmallIntegerField(default=1, verbose_name='Episode')),
                ('video', models.FileField(null=True, upload_to=movies.models.get_episode_path)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Season', verbose_name='Season')),
            ],
        ),
    ]
