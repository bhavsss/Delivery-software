# Generated by Django 3.2.4 on 2021-06-28 17:38

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
            name='BusinessDemoPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('section1', wagtail.core.fields.StreamField([('title', wagtail.core.blocks.CharBlock()), ('subtitle', wagtail.core.blocks.CharBlock())], blank=True, null=True)),
                ('section2', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock()), ('cards', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
