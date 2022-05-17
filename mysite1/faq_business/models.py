from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from .blocks import *


class FAQBusinessPage(Page):
    template = 'faq_business/faq_business_page.html'

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
            ('title1', blocks.CharBlock()),
            ('title2', blocks.CharBlock()),
            ('text_info', blocks.TextBlock()),
            ('image', ImageChooserBlock()),
            ('cta', CTABlock())
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
            ('heading1', blocks.CharBlock()),
            ('heading2', blocks.CharBlock()),
            ('partners', blocks.ListBlock(PartnerInfoBlock()))
        ],
        null=True,
        blank=True
    )

    section5 = StreamField(
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
    ]


