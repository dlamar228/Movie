from django.db import models
from django import forms
from django.urls import reverse

import os
from uuid import uuid1

def create_folder(path,name):
    result = os.path.join(path,name)
    os.mkdir(result)
    return result

def get_poster_path(instance,filename):
    return os.path.join('movies',instance.url,'poster',uuid1().hex+'.'+filename.split('.')[1])

def get_shots_path(instance,filename): 
    return os.path.join('movies',instance.movie.url,'shots',uuid1().hex + '.' +filename.split('.')[1])

def get_trailer_path(instance,filename): 
    return os.path.join('movies',instance.movie.url,'video','trailer',uuid1().hex + '.' +filename.split('.')[1])

def get_film_path(instance,filename): 
    return os.path.join('movies',instance.movie.url,'video','film',uuid1().hex + '.' +filename.split('.')[1])

def get_episode_path(instance,filename):
    return os.path.join('movies',instance.season.movie.url,'video','season_'+str(instance.season.season),uuid1().hex + '.' +filename.split('.')[1]) 

# Create your models here.
class Genre(models.Model):
    name = models.CharField("Name",max_length=100)
    description = models.TextField("Description")
    url = models.SlugField(max_length=160,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ganre"
        verbose_name_plural = "Ganres"

    def get_absolute_url(self):
        return reverse('movie_genre',kwargs = {'slug':self.url})

class Actor(models.Model):
    name = models.CharField("Name",max_length=100)
    description = models.TextField("Description")
    image = models.ImageField("Image",upload_to="media/actors/")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('actor_detail',kwargs = {'slug':self.name})

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"

class Country(models.Model):
    name = models.CharField("Country",max_length=30)
    
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countres"

    def __str__(self):
        return self.name

class Movie(models.Model):
    url = models.SlugField(max_length=160,unique=True)

    name = models.CharField("Name",max_length=100,blank=True)
    poster = models.ImageField("Poster",upload_to=get_poster_path ,blank = True)
    country =  models.ManyToManyField(Country,verbose_name = "Country", blank = True)

    year = models.PositiveSmallIntegerField("Date",default = 2019,blank=True)

    description_short = models.TextField("Short description", blank = True)
    description_detail = models.TextField("Detailed description", blank = True)

    actors = models.ManyToManyField(Actor,verbose_name = "Actor",related_name = "movie_actor" , blank = True)
    producers = models.ManyToManyField(Actor,verbose_name = "Producer",related_name = "movie_producer" , blank = True)

    genres = models.ManyToManyField(Genre,verbose_name = "Genre",  blank = True)

    completed = models.BooleanField("Сompleted",default = False)
    draft = models.BooleanField("Draft",default = False)
    

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def get_absolute_url(self):
        return reverse('movie_detail',kwargs = {'slug':self.url})

    def save(self, *args, **kwargs):
        if not os.path.exists('media\\movies\\'+self.url) :
            path = create_folder('media\\movies',self.url)
            create_folder(path,'poster')
            create_folder(path,'shots')
            path = create_folder(path,'video')
            create_folder(path,'trailer')
        super(Movie, self).save(*args, **kwargs)

class MovieShots(models.Model):
    movie = models.ForeignKey(Movie,verbose_name = "Movie",on_delete = models.CASCADE)
    description = models.TextField("Description")
    image = models.ImageField("Image",upload_to = get_shots_path)
      
    def __str__(self):        
        return self.description

    class Meta:
        verbose_name = "Shot"
        verbose_name_plural = "Shots"

class Season(models.Model):
    movie = models.ForeignKey(Movie,verbose_name = "Movie",on_delete = models.CASCADE)

    season = models.PositiveSmallIntegerField("Season",default = 1)
    episodes = models.PositiveSmallIntegerField("Episodes",default = 1)

    language = models.CharField("Language",max_length=20)
    voice_acting = models.CharField("Voice acting",max_length=50)
    quality = models.PositiveSmallIntegerField("Quality",default = 360) 

    description = models.TextField("Description", blank = True)   

class Episode(models.Model):
    season = models.ForeignKey(Season,verbose_name = "Season",on_delete = models.CASCADE)

    episode = models.PositiveSmallIntegerField("Episode",default = 1)

    video = models.FileField(upload_to = get_episode_path,null=True)

class Trailer(models.Model):
    movie = models.ForeignKey(Movie,verbose_name = "Movie",on_delete = models.CASCADE)

    language = models.CharField("Language",max_length=20)
    voice_acting = models.CharField("Voice acting",max_length=50)

    quality = models.PositiveSmallIntegerField("Quality",default = 360)

    video = models.FileField(upload_to = get_trailer_path,null=True)

class Film(models.Model):
    movie = models.ForeignKey(Movie,verbose_name = "Movie",on_delete = models.CASCADE)

    language = models.CharField("Language",max_length=20)
    voice_acting = models.CharField("Voice acting",max_length=50)

    quality = models.PositiveSmallIntegerField("Quality",default = 360)

    video = models.FileField(upload_to = get_film_path ,null=True)
