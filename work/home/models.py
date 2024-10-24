from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class HomePage(Page):
    # add the Hero section of HomePage:
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    description = models.CharField(
        blank=True,
        max_length=255, help_text="Write an introduction for the site"
    )
    # Call to Action (CTA): Incorporate a CTA that guides visitors to take a specific action, such as “View Portfolio,” “Hire Me,” or “Learn More”.
    specific_cta = models.CharField(
        blank=True,
        verbose_name="Specific CTA",
        max_length=255,
        help_text="Text to display on Call to Action",
    )
    specific_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Specific CTA link",
        help_text="Choose a page to link to for the Call to Action",
    )

    body = RichTextField(blank=True)

    # modify your content_panels:
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("image"),
                FieldPanel("description"),
                FieldPanel("specific_cta"),
                FieldPanel("specific_cta_link"),
            ],
            heading="Arctic Circle",
        ),
        FieldPanel('body'),
    ]
