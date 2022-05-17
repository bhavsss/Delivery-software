from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from .blocks import *


class BusinessServicesPage(Page):
    template = 'business_services/business_services_page.html'

    section1 = StreamField(
        [
            ('title', blocks.CharBlock()),
            ('tagline', blocks.CharBlock()),
            ('info_line', blocks.CharBlock()),
        ],
        null=True,
        blank=True
    )

    section2 = StreamField(
        [
            ('cards', blocks.ListBlock(TitleText()))
        ],
        null=True,
        blank=True
    )

    section3 = StreamField(
        [
            ('heading1', blocks.CharBlock()),
            ('heading2', blocks.CharBlock()),
            ('partners', blocks.ListBlock(PartnerInfo()))
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

    section5 = StreamField(
         [
             ('heading', blocks.CharBlock()),
         ],
         null=True,
         blank=True
    )

    section6 = StreamField(
        [
            ('heading1', blocks.CharBlock()),
            ('heading2', blocks.CharBlock()),
            ('text_info', blocks.CharBlock()),
            ('image', ImageChooserBlock()),
            ('cta', CTABlock())
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
            ('heading', blocks.CharBlock()),
            ('cards', blocks.ListBlock(ImageChooserBlock()))
        ],
        null=True,
        blank=True
    )

    section9 = StreamField(
        [
            ('heading1', blocks.CharBlock()),
            ('heading2', blocks.CharBlock()),
            ('points', blocks.ListBlock(TitleText()))
        ],
        null=True,
        blank=True
    )

    section10 = StreamField(
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
        StreamFieldPanel('section7'),
        StreamFieldPanel('section8'),
        StreamFieldPanel('section9'),
        StreamFieldPanel('section10'),
    ]


