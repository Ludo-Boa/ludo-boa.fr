from django.apps import AppConfig


class MyWorkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_work'
    verbose_name = "mes travaux"