from django.apps import AppConfig

class ScoreboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scoreboard'
    
    # def ready(self):
    #     from scoreboard_updater import updater
    #     updater.start()