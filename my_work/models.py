from io import BytesIO
import os
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.urls import reverse
from tinymce.models import HTMLField
from filer.fields.image import FilerImageField


def upload_to_original(instance, filename):
    return f'projects/images/original/{filename}'

def upload_to_thumbnail(size):
    return f'projects/images/thumb_{size}/'


# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name="nom", max_length=50)

    class Meta:
        verbose_name="catégorie de projet"

    def __str__(self) -> str:
        return self.name
    


class Project(models.Model):
    name = models.CharField(verbose_name="nom", max_length=150)
    url = models.URLField(blank=True)
    created = models.CharField(verbose_name="créé en", max_length=4, blank=True, help_text="année de création")
    image = FilerImageField(null=True, blank=True, on_delete=models.CASCADE, related_name="image_project")
    desc = HTMLField(verbose_name="description", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name="projet"

    
    """Renvoie l'URL permettant d'accéder à une instance particulière de film."""
    def get_absolute_url(self):
        return reverse("portfolio-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return self.name
    
