from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.fields import ImageField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from .blocks import *
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Page):
    template = 'home/home_page.html'

    section1 = StreamField(
        [
            ('heading1', blocks.CharBlock()),
            ('heading2', blocks.CharBlock()),
            ('info_line', blocks.CharBlock()),
            ('image', ImageChooserBlock())
        ],
        null=True,
        blank=True
    )

    section2 = StreamField(
        [
            ('heading1', blocks.CharBlock()),
            ('heading2', blocks.CharBlock()),
            ('info_line', blocks.RichTextBlock()),
            ('cta', CTABlock())
        ],
        null=True,
        blank=True
    )

    section3 = StreamField(
        [
            ('cards', blocks.ListBlock(TitleTextImageCTA()))
        ],
        null=True,
        blank=True
    )

    section4 = StreamField(
        [
            ('heading1', blocks.CharBlock()),
            ('heading2', blocks.CharBlock()),
            ('text_info', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('cta', CTABlock())
        ],
        null=True,
        blank=True
    )

    section5 = StreamField(
        [
            ('heading1', blocks.CharBlock()),
            ('heading2', blocks.CharBlock()),
            ('cards', blocks.ListBlock(CustomCard1()))
        ],
        null=True,
        blank=True
    )

    section6 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('cards', blocks.ListBlock(CustomCard2()))
        ],
        null=True,
        blank=True
    )

    section7 = StreamField(
        [
            ('heading1', blocks.CharBlock()),
            ('heading2', blocks.CharBlock()),
            ('cards', blocks.ListBlock(TitleText()))
        ],
        null=True,
        blank=True
    )

    section8 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('text_info', blocks.TextBlock()),
            ('ext_url', blocks.URLBlock())
        ],
        null=True,
        blank=True
    )

    section9 = StreamField(
        [
            ('text', blocks.CharBlock()),
            ('image', ImageChooserBlock()),
            ('cta', CTABlock())
        ],
        null=True,
        blank=True
    )

    section10 = StreamField(
        [
            ('heading1', blocks.CharBlock()),
            ('heading2', blocks.CharBlock()),
            ('info_line', blocks.CharBlock()),
            ('image', ImageChooserBlock()),
            ('cta', CTABlock())
        ],
        null=True,
        blank=True
    )

    section11 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('cards', blocks.ListBlock(ImageChooserBlock()))
        ],
        null=True,
        blank=True
    )

    section12 = StreamField(
        [],
        null=True,
        blank=True
    )

    section13 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('reviews', blocks.ListBlock(ReviewBlock()))
        ],
        null=True,
        blank=True
    )

    section14 = StreamField(
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
        StreamFieldPanel('section11'),
        StreamFieldPanel('section12'),
        StreamFieldPanel('section13'),
        StreamFieldPanel('section14'),
    ]
