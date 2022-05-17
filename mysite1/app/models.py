from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from .blocks import *


class AppPage(Page):
    template = 'app/app_page.html'

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
            ('image', ImageChooserBlock()),
            ('cta', CTABlock())
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('section1'),
        StreamFieldPanel('section2'),
    ]



