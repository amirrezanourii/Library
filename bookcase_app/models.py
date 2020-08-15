from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255, help_text="Enter a book genre")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary=
    isbn = 
    genre = 

    def __str__(self):
        


