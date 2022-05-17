from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleText(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.TextBlock()


class RichTitleText(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.RichTextBlock()



