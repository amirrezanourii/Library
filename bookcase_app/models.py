from django.db import models
from django.urls import reverse
import uuid
from accounts.models import User
from datetime import date


class Genre(models.Model):
    name = models.CharField(max_length=255, blank=True,
                            help_text="Enter a book genre")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1100, help_text='Description...')
    isbn = models.CharField(max_length=13, help_text='13 characters')
    genre = models.ManyToManyField(
        Genre, help_text='Select a genre', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bookcase_app:book_detail', args=[str(self.id)])


class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text='Book ID')
    return_back_day = models.DateField(blank=True, null=True)

    LOAN_STATUS = (('o', 'on loan'), 
                   ('a', 'available'),
                )

    status = models.CharField(max_length=1, choices=LOAN_STATUS,
                              blank=True, default='a', help_text='Book availability')
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.book.title

    class Meta:
        permissions = (( 'can_mark_returned', 'set_book_as_returned' ), )

    @property
    def is_overdue(self):
        if self.return_back_day and date.today() > self.return_back_day:
            return True
        return False


class Author(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.fname, self.lname}'
