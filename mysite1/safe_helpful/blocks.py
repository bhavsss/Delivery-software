from wagtail.core import blocks


class TitleText(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.CharBlock()


class CTABlock(blocks.StructBlock):
    button_page = blocks.PageChooserBlock()
    button_text = blocks.CharBlock()



