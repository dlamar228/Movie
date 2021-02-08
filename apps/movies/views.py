from django.shortcuts import render , redirect
from django.views.generic.base import View

from django.views.generic import ListView , DetailView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import Http404
from django.http.response import JsonResponse
from django.template.loader import render_to_string, get_template

from .models import Movie,Season,Episode,Film,Trailer
import json
# Create your views here.
class AjaxMoviesListView(ListView):
    model = Movie
    queryset = Movie.objects.all()
    template_name = "movies/movie-list.html"
    context_object_name = "movie_list"
    paginate_by = 9
    
    def get(self, request):
        paginate = self.paginate_page(self.queryset,self.get_page(request))
        return render(  request=request,
                        template_name=self.template_name,
                        context={self.context_object_name: paginate,
                                'page_obj': paginate}
                    )
    def post(self, request):
        genres = json.loads(request.POST.get('genres'))
        countres = json.loads(request.POST.get('countres'))
        years = json.loads(request.POST.get('years'))
        movie = self.filter(genres,countres,years)
        paginate = self.paginate_page(movie,self.get_page(request))
        if request.is_ajax():
            
            return JsonResponse({
                "movie_list": render_to_string(
                    request=request,
                    template_name='movies/movie-list-replace.html',
                    context={
                                self.context_object_name: paginate,
                                'page_obj': paginate
                            }
                ),
                'genres': genres,
                'countres': countres,
                "years": years,
            })
        else:
            raise Http404()
    def get_page(self,request ):
        return request.GET.get('page') if request.method == 'GET' else request.POST.get('page')
    def paginate_page(self,qr,page):
        paginate = self.get_paginator(qr,self.paginate_by)
        try:
            return paginate.page(page)
        except PageNotAnInteger:
            return paginate.page(1)
        except EmptyPage:
            return paginate.page(paginate.num_pages)
    def filter(self,genres,country,years):

        movie = self.queryset
        genres = list(map(int, genres))
        country = list(map(int, country))
        years = list(map(int, years))

        if len(genres) != 0:
            movie = movie.filter(genres__in = genres)
            movie = movie.distinct()

        if len(country) != 0:
            movie = movie.filter(country__in = country)
            

        if len(years) != 0:
            movie = movie.filter(year__in = years)

        movie = movie.distinct()
            
        return movie

class MoviesListView(ListView):
    model = Movie
    queryset = Movie.objects.all()

    template_name = "movies/movie-list.html"
    context_object_name = "movie_list"

    paginate_by = 1  
     
class MovieDetailView(DetailView):
    model = Movie
    template_name = "movies/movie-detail.html"
    slug_field = "url"

    def get_param(self,season,episodes):
        param = dict()
        for e in range(1,episodes+1):
            param[e] = dict()
        return param  
    def get_films_param(self,qr):
        for film in qr:
            if not film.language in param:
                param[film.language] = dict()
            elif not film.voice_acting in param[film.language]:
                param[film.language][film.voice_acting] = dict()

            param[film.language][film.voice_acting][film.quality] = film.video.url

        return param
    def get_seasons_param(self,qr):

        param = dict()
        for season in qr:
            if not season.language in param:
                param[season.language] = dict()
            if not season.voice_acting in param[season.language]:
                param[season.language][season.voice_acting] = dict()
            if not season.season in param[season.language][season.voice_acting]:  
                param[season.language][season.voice_acting][season.season] = self.get_param(season.season,season.episodes)

            for episode in Episode.objects.filter(season = season):
                param[season.language][season.voice_acting][season.season][episode.episode][season.quality] = episode.video.url

        return param     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        seasons = Season.objects.filter(movie = context['movie'])
        films = Film.objects.filter(movie = context['movie'])
        trailers = Trailer.objects.filter(movie = context['movie'])

        if len(seasons) > 0 :
            context['seasons'] = seasons
            context['param_s'] = json.dumps(self.get_seasons_param(seasons))
        if len(films) > 0 : 
            context['films'] = films
            context['param_f'] = json.dumps(self.get_films_param(films))
        if len(trailers) > 0 : 
            context['trailers'] = trailers
            context['param_t'] = json.dumps(self.get_films_param(trailers))

        return context
     