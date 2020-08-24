from django.shortcuts import render
from . import models
from django.views import generic 




def index(request):
    books_number = models.Book.objects.all().count()
    available_books = models.BookInstance.objects.filter(status__exact='a').count()

    return render(request, 'bookcase_app/index.html', context={'books_number': books_number, 'available_books': available_books})



class BookList(generic.ListView):
    model = models.Book
    template_name = 'book_list.html'

    
class BookDetailView(generic.DetailView):
    model = models.BookInstance
    template_name = 'book_detail.html'
