from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleDateTextImage(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    date = blocks.DateBlock(required=False)
    text = blocks.TextBlock(required=False)
    image = ImageChooserBlock(required=False)
    # page = blocks.PageChooserBlock(required=False)

