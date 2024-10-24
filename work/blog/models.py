from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from wagtail.snippets.models import register_snippet
from taggit.models import Tag as TaggitTag
from taggit.models import TaggedItemBase

from wagtail.search import index

from modelcluster.fields import ParentalKey


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True

class PostPageBlogCategory(models.Model):
    page = ParentalKey(
        "blog.BlogPage", on_delete=models.CASCADE, related_name="categories"
    )
    blog_category = models.ForeignKey(
        "blog.BlogCategory", on_delete=models.CASCADE, related_name="post_pages"
    )

    panels = [
        FieldPanel("blog_category"),
    ]

    class Meta:
        unique_together = ("page", "blog_category")


class PostPageTag(TaggedItemBase):
    content_object = ParentalKey("BlogPage", related_name="post_tags")
