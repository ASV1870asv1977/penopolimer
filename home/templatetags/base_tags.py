from django import template

from home.models import Footer, Header, ProductCardPages, EventNewsPages

register = template.Library()


@register.inclusion_tag('home/tags/header.html', takes_context=True)
def header_tag(context):
    return {
        'request': context['request'],
        'header': Header.objects.first(),
    }


@register.inclusion_tag('home/tags/footer.html', takes_context=True)
def footer_tag(context):
    return {
        'request': context['request'],
        'footer': Footer.objects.first(),
    }


@register.inclusion_tag('home/tags/product_card_page.html', takes_context=True)
def product_card_tag(context):
    return {
        'request': context['request'],
        'product_card': ProductCardPages.objects.first(),
    }


@register.inclusion_tag('home/tags/event_news_page.html', takes_context=True)
def event_news_tag(context):
    return {
        'request': context['request'],
        'event_news': EventNewsPages.objects.first(),
    }

