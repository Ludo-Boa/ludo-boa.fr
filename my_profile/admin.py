from django.contrib import admin
from django.utils.html import format_html
from .models import Experience, KnowHow, TechnicalSkills, Education, Social, Interest


# Register your models here.

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("job", "business", "date_end", "date_start")
    ordering = ["-date_end"]


@admin.register(TechnicalSkills)
class TechnicalSkillsAdmin(admin.ModelAdmin):
    list_display = ("name", 'tag')
    ordering = ["tag"]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    fields = [
        ("date_start", "date_end"), 
        ("title", "school"), 
        "city",
        ("level", "graduation"),
        "description",
    ]



admin.site.register(KnowHow)
admin.site.register(Social)
admin.site.register(Interest)


