from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class CTABlock(blocks.StructBlock):
    button_page = blocks.PageChooserBlock()
    button_text = blocks.CharBlock()


class ImageNumberText(blocks.StructBlock):
    image = ImageChooserBlock()
    number = blocks.IntegerBlock()
    text_info = blocks.TextBlock()


class ReviewBlock(blocks.StructBlock):
    review = blocks.TextBlock()
    person_name = blocks.CharBlock()
    person_info = blocks.CharBlock()
    person_image = ImageChooserBlock()


class CustomCard1(blocks.StructBlock):
    title = blocks.CharBlock()
    content = blocks.RichTextBlock()
    cta = CTABlock()


class TitleText(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.CharBlock()



