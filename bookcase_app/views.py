from django.shortcuts import render
from . import models


def index(request):
    books_number = Book.objects.all().count()
    available_books = BookInstance.objects.filter(status__exact='a').count()

    return render(request, 'index.html', context={'books_number': books_number, 'available_books': available_books})
