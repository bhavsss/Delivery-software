# Generated by Django 3.2.4 on 2021-06-25 18:19

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('section1', wagtail.core.fields.StreamField([('title', wagtail.core.blocks.CharBlock()), ('subtitle', wagtail.core.blocks.CharBlock()), ('list_title', wagtail.core.blocks.CharBlock()), ('list_points', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock())), ('bottom_line', wagtail.core.blocks.CharBlock())], blank=True, null=True)),
                ('section2', wagtail.core.fields.StreamField([('title', wagtail.core.blocks.CharBlock()), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.CharBlock())])))], blank=True, null=True)),
                ('section3', wagtail.core.fields.StreamField([('title', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.CharBlock()), ('video', wagtail.core.blocks.URLBlock())], blank=True, null=True)),
                ('section4', wagtail.core.fields.StreamField([('title', wagtail.core.blocks.CharBlock()), ('subtitle', wagtail.core.blocks.CharBlock()), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.CharBlock())])))], blank=True, null=True)),
                ('section5', wagtail.core.fields.StreamField([('title1', wagtail.core.blocks.CharBlock()), ('title2', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.CharBlock()), ('cta', wagtail.core.blocks.StructBlock([('button_page', wagtail.core.blocks.PageChooserBlock()), ('button_text', wagtail.core.blocks.CharBlock())])), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))], blank=True, null=True)),
                ('section6', wagtail.core.fields.StreamField([('title1', wagtail.core.blocks.CharBlock()), ('title2', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.CharBlock()), ('cta', wagtail.core.blocks.StructBlock([('button_page', wagtail.core.blocks.PageChooserBlock()), ('button_text', wagtail.core.blocks.CharBlock())])), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))], blank=True, null=True)),
                ('section7', wagtail.core.fields.StreamField([('reviews', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('review', wagtail.core.blocks.CharBlock()), ('person_name', wagtail.core.blocks.CharBlock()), ('person_designation', wagtail.core.blocks.CharBlock()), ('person_image', wagtail.images.blocks.ImageChooserBlock())])))], blank=True, null=True)),
                ('section8', wagtail.core.fields.StreamField([('title', wagtail.core.blocks.CharBlock()), ('cards', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))], blank=True, null=True)),
                ('section9', wagtail.core.fields.StreamField([('title', wagtail.core.blocks.CharBlock())], blank=True, null=True)),
                ('section10', wagtail.core.fields.StreamField([('title', wagtail.core.blocks.CharBlock()), ('subtitle', wagtail.core.blocks.CharBlock())], blank=True, null=True)),
                ('section11', wagtail.core.fields.StreamField([('banner_title', wagtail.core.blocks.CharBlock()), ('cta', wagtail.core.blocks.StructBlock([('button_page', wagtail.core.blocks.PageChooserBlock()), ('button_text', wagtail.core.blocks.CharBlock())]))], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]