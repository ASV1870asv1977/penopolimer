from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.core.fields import RichTextField

from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
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


class HomeSlidesImage(Orderable):
    """Изображения продукции для слайдов с описанием"""
    image_slide = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Изображение продукции',
    )

    product_name = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name="Название продукции",
    )

    # product_name = RichTextField(
    #     features=['enter'],
    #     blank=True,
    #     null=True,
    #     max_length=100,
    #     verbose_name="Название продукции",
    # )

    product_description = RichTextField(
        features=['enter'],
        blank=True,
        null=True,
        max_length=200,
        verbose_name="Описание продукции",
    )

    equipment = ParentalKey(
        'home.HomePage',
        on_delete=models.CASCADE,
        related_name='slides',
    )

    panels = [
        ImageChooserPanel('image_slide'),
        FieldPanel('product_name'),
        FieldPanel('product_description'),
    ]


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

    # name_page = models.CharField(
    #     max_length=100,
    #     blank=True,
    #     null=True,
    #     verbose_name="Подзаголовок",
    # )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            InlinePanel('slides', label='слайд')],
            heading='Слайды'),
    ]
    # content_panels = Page.content_panels + [
    #     FieldPanel('name_page'),
    # ]
