from django.contrib import admin
from django.utils.html import format_html
from .models import Movie, Genre


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:150px; max-height:150px"/>'.format(obj.poster.url))

    list_display = ("title", "display_genre", "production", "pub_date")
    

    readonly_fields = ['image_tag']
    fieldsets = [
        (None, {
            "fields": ["title", "production", ("year", "time", "genre"), "pub_date",]
        }),
        ("Image et vidéo", {
            "fields": [("poster", "image_tag"), "movie_file"]
        }),
        ("Paramètres", {"fields": ["slug"], "classes": ["collapse"]}),
        
        
    ]
    prepopulated_fields = {"slug": ["title"]}
    search_fields = ('title',)



admin.site.register(Genre)

    
