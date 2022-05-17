from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from .blocks import *


class FAQPage(Page):
    template = 'faq/faq_page.html'

    section1 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('image', ImageChooserBlock())
        ],
        null=True,
        blank=True
    )

    section2 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('cta', blocks.URLBlock())
        ],
        null=True,
        blank=True
    )

    section3 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('points', blocks.ListBlock(RichTitleText()))
        ],
        null=True,
        blank=True
    )

    section4 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('cards', blocks.ListBlock(TitleText()))
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('section1'),
        StreamFieldPanel('section2'),
        StreamFieldPanel('section3'),
        StreamFieldPanel('section4'),
    ]


