from django.conf import settings
from django.db import models


class CustomText(models.Model):
    "Generated Model"
    chart = models.URLField(
        null=True,
        blank=True,
    )


class HomePage(models.Model):
    "Generated Model"
    body = models.TextField()
