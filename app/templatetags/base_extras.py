"""
Simple tags to help render page:
- reverse_url nav active: https://www.turnkeylinux.org/blog/django-navbar
"""
from django import template

register = template.Library()


@register.filter(name='fieldtype')
def field_type(field):
    """
    Access the widget in form field and return the name of the class for
    conditional rendering
    Args:
        field: form field
    Returns: string of form field type
    """
    return field.field.widget.__class__.__name__
