from django.db import models
from django.urls import reverse
import uuid


class Genre(models.Model):
    name = models.CharField(max_length=255, blank=True, help_text="Enter a book genre")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1100, help_text='Description...')
    isbn = models.CharField(max_length=13, help_text='13 characters')
    genre = models.ManyToManyField(Genre, help_text='Select a genre', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


    #def display_genre(self):
    #    return ', '.join([ genre_name for genre in self.genre.all()[:3] ])
    #display_genre.short_description = 'Genre'


class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text='Book ID')
    return_back_day = models.DateField(blank=True, null=True)

    loan_status = (('o', 'on loan'), ('a', 'available'),
                   )

    status = models.CharField(max_length=1, choices=loan_status,
                              blank=True, default='a', help_text='Book availability')

    def __str__(self):
        return f'{self.id} {self.book.title}'



class Author(models.Model):
    fname = models.CharField(max_length= 200)
    lname = models.CharField(max_length= 200)
    birthday = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.fname, self.lname}'
