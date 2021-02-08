from django import template

from movies.models import Genre , Movie , Country

register = template.Library()

@register.simple_tag()
def get_geners():
    return Genre.objects.all()

@register.simple_tag()
def get_years(count = 30):
    result = Movie.objects.filter(draft = False)
    result = result.distinct()
    result = result.values_list('year',flat = True).order_by('-year')[:count]
    return result

@register.simple_tag()
def get_countres():
    return Country.objects.order_by('-id')

@register.simple_tag()
def get_last_movies(count = 6):
    return Movie.objects.order_by('-id')[:count]