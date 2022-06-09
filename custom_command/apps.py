from django.apps import AppConfig


class CustomCommandConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_command'
