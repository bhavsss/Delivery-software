from wagtail.core import blocks


class CTABlock(blocks.StructBlock):
    button_page = blocks.PageChooserBlock(required=False)
    button_text = blocks.CharBlock(required=False)


class TitleTextCTA(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.RichTextBlock()
    cta = CTABlock()


class List(blocks.StructBlock):
    title = blocks.CharBlock()
    points = blocks.ListBlock(blocks.TextBlock())
