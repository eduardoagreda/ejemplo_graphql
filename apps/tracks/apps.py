from django.apps import AppConfig


class TracksConfig(AppConfig):
    name = 'apps.tracks'
    
    def ready(self):
        import apps.tracks.signals