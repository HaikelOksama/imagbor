from django import template
from django.contrib.auth.models import Permission, User
from imabor.models import Image
register = template.Library()
#this will create custom tags for template
#in template use {% load %} to load the tags
@register.simple_tag
def nature_len():
    return Image.objects.filter(tags='nature').count()

@register.simple_tag
def animasi_len():
    return Image.objects.filter(tags='animasi').count()

@register.simple_tag
def building_len():
    return Image.objects.filter(tags='building').count()

@register.simple_tag
def space_len():
    return Image.objects.filter(tags='space').count()



