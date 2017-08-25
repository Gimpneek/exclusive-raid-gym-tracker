from django.db import models


class Gym(models.Model):
    """ Model to hold Gym information """

    name = models.CharField(max_length=256, help_text="Name of Gym")
    gym_hunter_id = models.CharField(max_length=32, help_text="ID on Gymhuntr")
    location = models.CharField(max_length=128, help_text="Location in long,lat format")
    image_url = models.CharField(max_length=256, help_text="URL of image used for Gym")

    def __str__(self):
        return self.name
