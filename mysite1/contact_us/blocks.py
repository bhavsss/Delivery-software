from wagtail.core import blocks


class TitleText(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.CharBlock()


