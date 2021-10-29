from django import template

from home.models import Footer

register = template.Library()


@register.inclusion_tag('home/tags/footer.html', takes_context=True)
def footer_tag(context):
    return {
        'request': context['request'],
        'footer': Footer.objects.first(),
    }
