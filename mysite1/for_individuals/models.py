from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from .blocks import *


class ForIndividualsPage(Page):
    template = 'for_individuals/for_individuals_page.html'

    section1 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('text_info', blocks.CharBlock()),
            ('cta', CTABlock()),
            ('image', ImageChooserBlock())
        ],
        null=True,
        blank=True
    )

    section2 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('cards', blocks.ListBlock(ImageChooserBlock()))
        ],
        null=True,
        blank=True
    )

    section3 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('cards', blocks.ListBlock(ImageNumberText()))
        ],
        null=True,
        blank=True
    )

    section4 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('cards', blocks.ListBlock(ImageChooserBlock()))
        ],
        null=True,
        blank=True
    )

    section5 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('reviews', blocks.ListBlock(ReviewBlock()))
        ],
        null=True,
        blank=True
    )

    section6 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('text_info', blocks.CharBlock()),
            ('cta', blocks.URLBlock())
        ],
        null=True,
        blank=True
    )

    section7 = StreamField(
        [
            ('heading1', blocks.CharBlock()),
            ('heading2', blocks.CharBlock()),
            ('text_info', blocks.TextBlock()),
            ('cta', CTABlock()),
            ('image', ImageChooserBlock())
        ],
        null=True,
        blank=True
    )

    section8 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('cards', blocks.ListBlock(CustomCard1()))
        ],
        null=True,
        blank=True
    )

    section9 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('cards', blocks.ListBlock(TitleText()))
        ],
        null=True,
        blank=True
    )

    section10 = StreamField(
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
        StreamFieldPanel('section8'),
        StreamFieldPanel('section9'),
        StreamFieldPanel('section10'),
    ]


