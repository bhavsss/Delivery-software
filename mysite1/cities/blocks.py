from wagtail.core import blocks


class CTABlock(blocks.StructBlock):
    button_page = blocks.PageChooserBlock()
    button_text = blocks.CharBlock()


class TitleTextCTA(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.TextBlock()
    cta = CTABlock()

