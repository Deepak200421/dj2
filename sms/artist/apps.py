from django.apps import AppConfig


class ArtistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'artist'

class RazorpayIntegrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'razorpay_integration'
