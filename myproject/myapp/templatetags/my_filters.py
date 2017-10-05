from django import template
register = template.Library()

@register.filter(name='times') 
def times(number):
    return range(number)

@register.filter(name='pagina4') 
def pagina4(number):
    return int(number/4)

@register.filter(name='pagina8') 
def pagina8(number):
    return int(number/8)

@register.filter(name='count') 
def count(count):
    return len(count)
