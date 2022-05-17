from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleText(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.CharBlock()


class Review(blocks.StructBlock):
    review = blocks.CharBlock()
    person_name = blocks.CharBlock()
    person_designation = blocks.CharBlock()
    person_image = ImageChooserBlock()


class CTABlock(blocks.StructBlock):
    button_page = blocks.PageChooserBlock()
    button_text = blocks.CharBlock()


