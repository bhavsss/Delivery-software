from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from .blocks import *


class BlogDetailPage(Page):
    template = 'blog_detail/blog_detail_page.html'

    section1 = StreamField(
        [
            ('title', blocks.CharBlock()),
            ('date', blocks.DateBlock()),
            ('image', ImageChooserBlock())
        ],
        null=True,
        blank=True
    )

    section2 = StreamField(
        [
            ('text', blocks.RichTextBlock()),
        ],
        null=True,
        blank=True
    )

    section3 = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('cards', blocks.ListBlock(TitleTextCTA()))
        ],
        null=True,
        blank=True
    )

    section4 = StreamField(
        [
            ('title', blocks.CharBlock()),
            ('text', blocks.RichTextBlock())
        ],
        null=True,
        blank=True
    )

    section5 = StreamField(
        [
            ('part1', List()),
        ]
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('section1'),
        StreamFieldPanel('section2'),
        StreamFieldPanel('section3'),
        StreamFieldPanel('section4'),
        StreamFieldPanel('section5'),
    ]


