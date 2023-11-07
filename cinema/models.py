import datetime

from typing import Any
from django.db import models
from django.urls import reverse
from easy_thumbnails.fields import ThumbnailerImageField
from django.utils import timezone
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField


class Genre(models.Model):
    """Modèle représentant un genre de film."""
    name = models.CharField('nom', max_length=155, help_text="Entrez un genre de film")

    # Metadata
    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
        ordering = ['name']

    """Renvoie l'URL permettant d'accéder à une instance particulière du modèle Genre."""
    def get_absolute_url(self):
        return reverse("genre-detail", args=[str(self.id)])
    

    def __str__(self) -> str:
        """Chaîne pour représenter l'objet MyModelName (dans le site d'administration, etc.)."""
        return f"{self.name }"


class Movie(models.Model):
    """Modèle représentant un film (mais pas un exemplaire spécifique d'un film)."""
    title = models.CharField('titre', max_length=155)
    poster = FilerImageField(null=True, blank=True, on_delete=models.CASCADE, related_name="poster_movie")
    movie_file = FilerFileField(null=True, blank=True, on_delete=models.CASCADE, related_name="file_movie")
    genre = models.ManyToManyField(Genre, verbose_name="genre", help_text="Sélectionnez un genre pour ce film /", blank=True)
    slug = models.SlugField("URL", max_length=255, blank=False, null=False, default="")
    year = models.IntegerField("année", null=True, blank=True)
    time = models.TimeField("durée", default=datetime.time(00,00), blank=True)
    production = models.CharField(max_length=255, blank=True)
    pub_date = models.DateTimeField("date de publication", null=True)
    
    
    class Meta:
        verbose_name = "Film"
        ordering = ['title']

    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=15)
    

    def display_genre(self):
        """Créez une chaîne pour le genre. Ceci est nécessaire pour afficher le genre dans l’administrateur."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

    """Renvoie l'URL permettant d'accéder à une instance particulière de film."""
    def get_absolute_url(self):
        return reverse("movie-detail", args=[str(self.slug)])

    def __str__(self) -> str:
        return f"{self.title }"
    
