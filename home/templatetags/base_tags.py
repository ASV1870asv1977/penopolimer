from django import template

from home.models import Footer

register = template.Library()


@register.inclusion_tag('home/tags/header.html', takes_context=True)
def header_tag(context):
    return {
        'request': context['request'],
        'header': Footer.objects.first(),
    }


@register.inclusion_tag('home/tags/footer.html', takes_context=True)
def footer_tag(context):
    return {
        'request': context['request'],
        'footer': Footer.objects.first(),
    }
