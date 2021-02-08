# Generated by Django 3.0.5 on 2020-11-14 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0014_auto_20201114_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=models.CharField(blank=True, max_length=30, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(blank=True, max_length=100, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, default=2019, verbose_name='Date'),
        ),
    ]
