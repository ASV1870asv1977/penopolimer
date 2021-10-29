from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField

from wagtail.core.models import Page
from wagtail.snippets.models import register_snippet


@register_snippet
class Header(models.Model):

    telephones = RichTextField(
        features=['enter'],
        max_length=100,
        verbose_name="Телефоны предприятия",
    )

    address = RichTextField(
        features=['enter'],
        max_length=100,
        verbose_name="Адрес предприятия",
    )

    panels = [
        FieldPanel('telephones'),
        FieldPanel('address'),
    ]

    class Meta:
        verbose_name = 'Хедер'
        verbose_name_plural = 'Хедеры'

    def __str__(self):
        return 'Хедер'


@register_snippet
class Footer(models.Model):

    address = RichTextField(
        features=['enter'],
        max_length=100,
        verbose_name="Адрес предприятия",
    )

    telephones = RichTextField(
        features=['enter'],
        max_length=100,
        verbose_name="Телефоны предприятия",
    )

    email = models.EmailField(
        verbose_name="Email предприятия",
    )

    panels = [
        FieldPanel('address'),
        FieldPanel('telephones'),
        FieldPanel('email'),
    ]

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футеры'

    def __str__(self):
        return 'Футер'


class CalendarPage(Page):
    """Календарь"""
    max_count = 1


class PhotoGalleryPage(Page):
    """Фотогалерея"""
    max_count = 1


class ContactsPage(Page):
    """Контакты"""
    max_count = 1


class FormPage(Page):
    """Сделать заказ"""
    max_count = 1


class FagPage(Page):
    """Вопросы и ответы"""
    max_count = 1


class LibraryPage(Page):
    """Библиотека"""
    max_count = 1


class AboutPage(Page):
    """О компании"""
    max_count = 1


class HomePage(Page):
    """Главная"""

    subpage_types = [
        'home.AboutPage',
        'home.LibraryPage',
        'home.FagPage',
        'home.FormPage',
        'home.ContactsPage',
        'home.PhotoGalleryPage',
        'home.CalendarPage',
    ]

    parent_page_types = []

    name_page = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Подзаголовок",
    )

    content_panels = Page.content_panels + [
        FieldPanel('name_page'),
    ]




