from django import template

register = template.Library()

@register.filter(name='addClass')
def addClass(value, arg):
    return value.as_widget(attrs={'class': arg})

@register.filter(name='addPlaceholder')
def addPlaceholder(value, arg):
    return value.as_widget(attrs={'placeholder': arg})