from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from .blocks import *


class ServicePage(Page):
    template = 'service/service_page.html'

    section1 = StreamField(
        [
            ('banner_title', blocks.CharBlock()),
            ('banner_subtitle', blocks.CharBlock()),
            ('banner_image', ImageChooserBlock())
        ],
        null=True,
        blank=True
    )

    section2 = StreamField(
        [
            ('image', ImageChooserBlock()),
            ('heading', blocks.CharBlock()),
            ('text_info', blocks.CharBlock()),
            ('points', blocks.ListBlock(TitleText()))
        ],
        null=True,
        blank=True
    )

    section3 = StreamField(
        [
            ('image', ImageChooserBlock()),
            ('heading', blocks.CharBlock()),
            ('text_info', blocks.CharBlock()),
            ('points', blocks.ListBlock(TitleText()))
        ],
        null=True,
        blank=True
    )

    section4 = StreamField(
        [
            ('image', ImageChooserBlock()),
            ('heading', blocks.CharBlock()),
            ('text_info', blocks.CharBlock()),
            ('points', blocks.ListBlock(TitleText()))
        ],
        null=True,
        blank=True
    )

    section5 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('cards', blocks.ListBlock(TitleTextCTA()))
        ],
        null=True,
        blank=True
    )

    section6 = StreamField(
        [
            ('review', blocks.TextBlock()),
            ('image', ImageChooserBlock()),
            ('name', blocks.CharBlock())
        ],
        null=True,
        blank=True
    )

    section7 = StreamField(
        [
            ('cta', CTABlock())
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('section1'),
        StreamFieldPanel('section2'),
        StreamFieldPanel('section3'),
        StreamFieldPanel('section4'),
        StreamFieldPanel('section5'),
        StreamFieldPanel('section6'),
        StreamFieldPanel('section7'),
    ]


