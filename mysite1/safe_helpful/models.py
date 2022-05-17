from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from .blocks import *


class SafeHelpfulPage(Page):
    template = 'safe_helpful/safe_helpful_page.html'

    section1 = StreamField(
        [
            ('heading_image', ImageChooserBlock()),
            ('image', ImageChooserBlock()),
            ('text_info', blocks.TextBlock()),
            ('points', blocks.ListBlock(TitleText())),
            ('cta', CTABlock())
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('section1'),
    ]


