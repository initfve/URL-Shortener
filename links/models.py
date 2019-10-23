from django.db import models


class Link(models.Model):
    orginal_url = models.URLField()
    short_url = models.CharField(max_length=10)
    clicked = models.PositiveIntegerField()
