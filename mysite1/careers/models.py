from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from .blocks import *


class CareersPage(Page):
    template = 'careers/careers_page.html'

    section1 = StreamField(
        [
            ('banner_title', blocks.CharBlock()),
            ('banner_image', ImageChooserBlock())

        ],
        null=True,
        blank=True
    )

    section2 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('cards', blocks.ListBlock(TitleText()))
        ],
        null=True,
        blank=True
    )

    section3 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('cards', blocks.ListBlock(TitleTextImage()))
        ],
        null=True,
        blank=True
    )

    section4 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('points', blocks.ListBlock(blocks.CharBlock()))
        ],
        null=True,
        blank=True
    )

    section5 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('openings', blocks.ListBlock(AvailableRoles()))
        ],
        null=True,
        blank=True
    )

    section6 = StreamField(
        [
            ('heading1', blocks.CharBlock()),
            ('heading2', blocks.CharBlock()),
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
    ]


