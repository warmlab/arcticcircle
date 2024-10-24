# Generated by Django 5.0.9 on 2024-10-21 04:57

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliopage',
            name='body',
            field=wagtail.fields.StreamField([('heading_block', 2), ('paragraph_block', 3), ('image_block', 6), ('embed_block', 7), ('card', 11), ('featured_posts', 15)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'form_classname': 'title', 'required': True}), 1: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('', 'Select a heading size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], 'required': False}), 2: ('wagtail.blocks.StructBlock', [[('heading_text', 0), ('size', 1)]], {}), 3: ('wagtail.blocks.RichTextBlock', (), {'icon': 'pilcrow'}), 4: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 5: ('wagtail.blocks.CharBlock', (), {'required': False}), 6: ('wagtail.blocks.StructBlock', [[('image', 4), ('caption', 5), ('attribution', 5)]], {}), 7: ('wagtail.embeds.blocks.EmbedBlock', (), {'help_text': 'Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks', 'icon': 'media'}), 8: ('wagtail.blocks.CharBlock', (), {}), 9: ('wagtail.blocks.RichTextBlock', (), {'features': ['bold', 'italic', 'link']}), 10: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': False}), 11: ('wagtail.blocks.StructBlock', [[('heading', 8), ('text', 9), ('image', 10)]], {'group': 'Sections'}), 12: ('wagtail.blocks.RichTextBlock', (), {'features': ['bold', 'italic', 'link'], 'required': False}), 13: ('wagtail.blocks.PageChooserBlock', (), {'page_type': ['blog.BlogPage']}), 14: ('wagtail.blocks.ListBlock', (13,), {}), 15: ('wagtail.blocks.StructBlock', [[('heading', 8), ('text', 12), ('posts', 14)]], {'group': 'Sections'})}, help_text='Use this section to list your projects and skills.'),
        ),
    ]