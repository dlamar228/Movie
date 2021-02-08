from django.template.defaulttags import register
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_all_lang(dictionary):
    return dictionary.keys()
    
@register.filter 
def get_all_voice(dictionary):
    result = set()
    for key in dictionary.keys():
        for value in dictionary[key].keys():
            result.add(value)
    return result