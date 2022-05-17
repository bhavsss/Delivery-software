from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleText(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.CharBlock()


class PersonInfo(blocks.StructBlock):
    image = ImageChooserBlock()
    name = blocks.CharBlock()
    designation = blocks.CharBlock()


class CTA(blocks.StructBlock):
    button_page = blocks.PageChooserBlock()
    button_text = blocks.CharBlock()

