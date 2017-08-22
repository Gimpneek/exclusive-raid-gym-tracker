from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    pokemon_go_username = models.CharField(max_length=128, help_text="Your name in Pokemon Go")

    def __unicode__(self):
        return self.pokemon_go_username
