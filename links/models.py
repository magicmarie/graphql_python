from django.db import models
from django.conf import settings


class Link(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True, max_length=200)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE, default=None)


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    link = models.ForeignKey('links.Link', related_name='votes', on_delete=models.CASCADE)
