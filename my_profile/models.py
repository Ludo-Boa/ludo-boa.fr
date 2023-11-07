from django.db import models
from tinymce.models import HTMLField


# Create your models here.

class Experience(models.Model):
    date_start = models.DateField('date de début')
    date_end = models.DateField('date de fin', blank=True)
    job = models.CharField('poste', max_length=155)
    business = models.CharField('entreprise', max_length=155)
    city = models.CharField('ville', max_length=50)
    task_description = HTMLField('description')

    def __str__(self):
        return self.job
    

class KnowHow(models.Model):
    name = models.CharField('compétence', max_length=50, blank=True,)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "compétence et savoir-faire"
        verbose_name_plural = "compétences et savoir-faire"


class TechnicalSkills(models.Model):
    TECHNICAL_SKILLS_TAGS = [
        ("SYSTEME", "Système"),
        ("BUREAUTIQUE", "Bureautique"),
        ("GRAPHISME", "Graphisme"),
        ("FRAMEWORK", "Framework"),
        ("PROGRAMMATION", "Programmation"),

    ]


    name = models.CharField('compétence technique', max_length=50, blank=True)
    tag = models.CharField(max_length=15, choices=TECHNICAL_SKILLS_TAGS)
    icon = models.CharField(max_length=50, verbose_name="icone", help_text="Nom de l'icone sur Devicon", blank=True)
    

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "compétence technique"
        verbose_name_plural = "compétences techniques"


class Education(models.Model):

    LEVEL_EDUCATION = [
        ("CAP", "CAP"),
        ("BEP", "BEP"),
        ("BAC", "BAC"),
        ("BAC+2", "BAC+2"),
        ("BAC+3", "BAC+3"),
        ("BAC+4", "BAC+4"),
        ("BAC+5", "BAC+5"),
        ("BAC+8", "BAC+8"),
    ]

    date_start = models.DateField('date de début')
    date_end = models.DateField('date de fin')
    title = models.CharField('titre', max_length=155)
    school = models.CharField('école', max_length=155)
    city = models.CharField('ville', max_length=50)
    level = models.CharField('niveau', max_length=7, choices=LEVEL_EDUCATION)
    graduation = models.BooleanField('diplôme obtenu', default=False)
    description = HTMLField('description', blank=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ["-date_end"]
        verbose_name = "formation"
        verbose_name_plural = "formations"


class Social(models.Model):

    FACEBOOK = 'FACEBOOK'
    LINKEDIN = 'LINKEDIN'
    INSTAGRAM = 'INSTAGRAM'
    CODEPEN = 'CODEPEN'
    GITHUB = 'GITHUB'
    TWITTER = 'TWITTER'

    SOCIAL_CHOICES = (
        (FACEBOOK, "Facebook"),
        (LINKEDIN, "Linkedin"),
        (INSTAGRAM, "Instagram"),
        (CODEPEN, "Codepen"),
        (GITHUB, "Github"),
        (TWITTER, "Twitter"),
    )
    
    name = models.CharField(max_length=9, choices=SOCIAL_CHOICES, verbose_name="nom")
    link = models.URLField(verbose_name="lien", max_length=255, blank=True)

    def __str__(self) -> str:
        return self.name
    

class Interest(models.Model):
    name = models.CharField(max_length=155, verbose_name="nom", blank=True)

    class Meta:
        verbose_name = "intérêt"
        verbose_name_plural = "intérêts"

    def __str__(self) -> str:
        return self.name



    

