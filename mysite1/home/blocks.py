from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class CTABlock(blocks.StructBlock):
    button_page = blocks.PageChooserBlock()
    button_text = blocks.CharBlock()


class TitleTextImageCTA(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.TextBlock()
    image = ImageChooserBlock()
    cta = CTABlock()


class CustomCard1(blocks.StructBlock):
    logo = blocks.CharBlock()
    title = blocks.CharBlock()
    text = blocks.CharBlock()


class CustomCard2(blocks.StructBlock):
    number = blocks.IntegerBlock()
    title = blocks.CharBlock()
    text = blocks.TextBlock()
    image = ImageChooserBlock()


class TitleText(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.CharBlock()


class ReviewBlock(blocks.StructBlock):
    review = blocks.TextBlock()
    person_image = ImageChooserBlock()
    person_name = blocks.CharBlock()
    person_info = blocks.CharBlock()

