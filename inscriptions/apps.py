from django.apps import AppConfig


class InscriptionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inscriptions'

    def ready (self):
        import inscriptions.signals
