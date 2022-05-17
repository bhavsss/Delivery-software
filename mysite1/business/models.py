from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from .blocks import *


class BusinessPage(Page):
    template = 'business/business_page.html'

    section1 = StreamField(
        [
            ('title', blocks.CharBlock()),
            ('subtitle', blocks.CharBlock()),
            ('list_title', blocks.CharBlock()),
            ('list_points', blocks.ListBlock(blocks.CharBlock())),
            ('bottom_line', blocks.CharBlock()),
        ],
        null=True,
        blank=True
    )

    section2 = StreamField(
        [
            ('title', blocks.CharBlock()),
            ('cards', blocks.ListBlock(TitleText()))
        ],
        null=True,
        blank=True
    )

    section3 = StreamField(
        [
            ('title', blocks.CharBlock()),
            ('text', blocks.CharBlock()),
            ('video', blocks.URLBlock()),
        ],
        null=True,
        blank=True
    )

    section4 = StreamField(
        [
            ('title', blocks.CharBlock()),
            ('subtitle', blocks.CharBlock()),
            ('cards', blocks.ListBlock(TitleText()))
        ],
        null=True,
        blank=True
    )

    section5 = StreamField(
        [
            ('title1', blocks.CharBlock()),
            ('title2', blocks.CharBlock()),
            ('text', blocks.CharBlock()),
            ('cta', CTABlock()),
            ('image', ImageChooserBlock(required=False))
        ],
        null=True,
        blank=True
    )

    section6 = StreamField(
        [
            ('title1', blocks.CharBlock()),
            ('title2', blocks.CharBlock()),
            ('text', blocks.CharBlock()),
            ('cta', CTABlock()),
            ('image', ImageChooserBlock(required=False))
        ],
        null=True,
        blank=True
    )

    section7 = StreamField(
        [
            ('reviews', blocks.ListBlock(Review()))
        ],
        null=True,
        blank=True
    )

    section8 = StreamField(
        [
            ('title', blocks.CharBlock()),
            ('cards', blocks.ListBlock(ImageChooserBlock()))
        ],
        null=True,
        blank=True
    )

    section9 = StreamField(
        [
            ('title', blocks.CharBlock()),
        ],
        null=True,
        blank=True
    )

    section10 = StreamField(
        [
            ('title', blocks.CharBlock()),
            ('subtitle', blocks.CharBlock()),
        ],
        null=True,
        blank=True
    )

    section11 = StreamField(
        [
            ('banner_title', blocks.CharBlock()),
            ('cta', CTABlock()),
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
        StreamFieldPanel('section8'),
        StreamFieldPanel('section9'),
        StreamFieldPanel('section10'),
        StreamFieldPanel('section11'),
    ]


