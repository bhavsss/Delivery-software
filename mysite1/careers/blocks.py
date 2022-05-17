from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleText(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.TextBlock()


class TitleTextImage(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.TextBlock()
    image = ImageChooserBlock()


class AvailableRoles(blocks.StructBlock):
    role = blocks.CharBlock()
    location = blocks.CharBlock()
    date_posted = blocks.DateBlock()
    duration = None


class CTABlock(blocks.StructBlock):
    button_page = blocks.PageChooserBlock()
    button_text = blocks.CharBlock()


