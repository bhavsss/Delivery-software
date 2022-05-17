from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks as blocks
from .blocks import TitleDateTextImage


class BlogPage(Page):
    template = 'blog/blog_page.html'

    section1 = StreamField(
        [
            ('cards', blocks.ListBlock(TitleDateTextImage())),
        ],
        null=True,
        blank=True
    )

    section2 = StreamField(
        [
            ('content', TitleDateTextImage()),
        ],
        null=True,
        blank=True
    )

    section3 = StreamField(
        [
            ('cards', blocks.ListBlock(TitleDateTextImage())),
        ],
        null=True,
        blank=True
    )

    section4 = StreamField(
        [
            ('cards', blocks.ListBlock(TitleDateTextImage())),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('section1'),
        StreamFieldPanel('section2'),
        StreamFieldPanel('section3'),
        StreamFieldPanel('section4'),
    ]


