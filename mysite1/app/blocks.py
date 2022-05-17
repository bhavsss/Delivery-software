from wagtail.core import blocks


class CTABlock(blocks.StructBlock):
    button_page = blocks.PageChooserBlock()
    button_text = blocks.CharBlock()


