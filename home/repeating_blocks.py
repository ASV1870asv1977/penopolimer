from wagtail.core.blocks import StructBlock, CharBlock
from wagtail.images.blocks import ImageChooserBlock


class ProductCardBlock(StructBlock):

    product_image = ImageChooserBlock(label='Изображение продукта')
    product_name = CharBlock(label='Название продукта')
    product_description = CharBlock(label='Описание продукта')

    class Meta:
        template = 'blocks/product_card.html'
        label = 'Карточка продукта'
