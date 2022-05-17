from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleText(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.TextBlock()


class CTABlock(blocks.StructBlock):
    button_page = blocks.PageChooserBlock()
    button_text = blocks.CharBlock()


class TitleTextCTA(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.TextBlock()
    cta = CTABlock()




