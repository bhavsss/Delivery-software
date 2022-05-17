# Generated by Django 3.2.4 on 2021-06-16 20:22

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutuspage',
            name='banner1_content',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.RichTextBlock()), ('title_text_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', max_length=100, required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add your text content', max_length=500, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image', required=False))]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='page_heading',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]