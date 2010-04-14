from django import template
register = template.Library()

@register.filter(name="hasattr")
def hasattr_filter(value, arg):
   return hasattr(value, arg)
