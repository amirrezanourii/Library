from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255, help_text="Enter a book genre")
    