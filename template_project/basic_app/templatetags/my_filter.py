from django import template

register = template.Library()

@register.filter(name="my_cut_upper")  # decorator
def my_cut_upper(value,arg):
    """
        this cuts out all values of "arg" from the string
    """
    return (value.replace(arg,"")).upper()

# register.filter("my_cut_upper",my_cut_upper)
