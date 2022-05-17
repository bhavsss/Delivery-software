from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class ImageText(blocks.StructBlock):
    img = ImageChooserBlock()
    text = blocks.CharBlock()


class CustomCard1(blocks.StructBlock):
    img = ImageChooserBlock()
    name = blocks.CharBlock()
    tag = blocks.CharBlock()
    price_delivery = blocks.CharBlock()
    estimated_time = blocks.CharBlock()



