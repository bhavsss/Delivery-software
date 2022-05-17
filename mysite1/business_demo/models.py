from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from .blocks import *


class BusinessDemoPage(Page):
    template = 'business_demo/business_demo_page.html'

    section1 = StreamField(
        [
            ('title', blocks.CharBlock()),
            ('subtitle', blocks.CharBlock()),
        ],
        null=True,
        blank=True
    )

    section2 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('cards', blocks.ListBlock(ImageChooserBlock()))
        ]
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('section1'),
        StreamFieldPanel('section2'),
    ]


