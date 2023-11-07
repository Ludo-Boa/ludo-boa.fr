from django.contrib import admin
from django.utils.html import format_html
from .models import Project, Category

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    def vignette(self, obj):
        return format_html('<img src="{}" style="max-width:300px; height:auto; max-height:150px"/>'.format(obj.image.url))

    readonly_fields = ['vignette']

    fieldsets = [
        (None, {
            "fields": [("name", "category", "created"), ("image", "vignette"), "url", "desc"],
        }),
       
    ]


admin.site.register(Category)