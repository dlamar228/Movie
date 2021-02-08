from django.urls import path , include

from . import views

urlpatterns = [
    #path('home/',views.MoviesListView.as_view(), name = 'home'), 
    path('home/',views.AjaxMoviesListView.as_view(), name = 'home'), 
    path('<slug:slug>/',views.MovieDetailView.as_view(),name = 'movie_detail'),
]