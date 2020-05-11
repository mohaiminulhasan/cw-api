from django.db.models.signals import pre_save
from django.dispatch import receiver

from django.utils.text import slugify

from .models import Category, Brand, Model, Variant

@receiver(pre_save, sender=Brand)
def create_brand_slug(instance, **kwargs):
    slug = "{category}-{brand}".format(
        category = instance.category.slug,
        brand = slugify(instance.name)
    )
    instance.slug = slug

@receiver(pre_save, sender=Model)
def create_model_slug(instance, **kwargs):
    slug = "{brand}-{model}".format(
        brand = instance.brand.slug,
        model = slugify(instance.name)
    )
    instance.slug = slug

@receiver(pre_save, sender=Variant)
def create_variant_slug(instance, **kwargs):
    slug = "{model}-{variant}".format(
        model=instance.model.slug,
        variant=slugify(instance.name)
    )
    instance.slug = slug
