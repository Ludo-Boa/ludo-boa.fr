# Generated by Django 4.2.7 on 2023-11-07 10:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filer', '0017_image__transparent'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Entrez un genre de film', max_length=155, verbose_name='nom')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='titre')),
                ('slug', models.SlugField(default='', max_length=255, verbose_name='URL')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='année')),
                ('time', models.TimeField(blank=True, default=datetime.time(0, 0), verbose_name='durée')),
                ('production', models.CharField(blank=True, max_length=255)),
                ('pub_date', models.DateTimeField(null=True, verbose_name='date de publication')),
                ('genre', models.ManyToManyField(blank=True, help_text='Sélectionnez un genre pour ce film /', to='cinema.genre', verbose_name='genre')),
                ('movie_file', filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_movie', to='filer.file')),
                ('poster', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='poster_movie', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'verbose_name': 'Film',
                'ordering': ['title'],
            },
        ),
    ]