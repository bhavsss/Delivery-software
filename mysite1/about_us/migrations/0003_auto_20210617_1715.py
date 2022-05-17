# Generated by Django 3.2.4 on 2021-06-17 11:45

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0002_auto_20210617_0152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutuspage',
            name='banner1_content',
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='section1',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.RichTextBlock()), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', max_length=100, required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add your text content', max_length=500, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image', required=False))])))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='section2',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.RichTextBlock()), ('tagline', wagtail.core.blocks.RichTextBlock())], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='section3',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.RichTextBlock()), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', max_length=100, required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add your text content', max_length=500, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image', required=False))])))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='section4',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.RichTextBlock()), ('text', wagtail.core.blocks.RichTextBlock())], blank=True, null=True),
        ),
    ]
