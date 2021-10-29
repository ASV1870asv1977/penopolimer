from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.core.models import Page


class PhotoGalleryPage(Page):
    """Фотогалерея"""
    pass


class ContactsPage(Page):
    """Контакты"""
    pass


class FormPage(Page):
    """Сделать заказ"""
    pass


class FagPage(Page):
    """Вопросы и ответы"""
    pass


class LibraryPage(Page):
    """Библиотека"""
    pass


class AboutPage(Page):
    """О компании"""
    pass


class HomePage(Page):
    """Главная"""

    subpage_types = [
        'home.AboutPage',
        'home.LibraryPage',
        'home.FagPage',
        'home.FormPage',
        'home.ContactsPage',
        'home.PhotoGalleryPage',
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




