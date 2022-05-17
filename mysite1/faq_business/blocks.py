from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class CTABlock(blocks.StructBlock):
    button_page = blocks.PageChooserBlock()
    button_text = blocks.CharBlock()


class TitleText(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.TextBlock()


class RichTitleText(blocks.StructBlock):
    title = blocks.TextBlock()
    text = blocks.RichTextBlock()


class PartnerInfoBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    service = blocks.CharBlock()
    points = blocks.ListBlock(TitleText())



