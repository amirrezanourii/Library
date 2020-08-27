from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView
from . import models


# def index(request):
#     books_number = models.Book.objects.all().count()
#     available_books = models.BookInstance.objects.filter(
#         status__exact='a').count()

#     return render(request, 'bookcase_app/index.html', context={'books_number': books_number, 'available_books': available_books})


class Index(generic.TemplateView):
    template_name = 'bookcase_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books_number'] = models.Book.objects.all().count()
        context['available_books'] = models.BookInstance.objects.filter(
            status__exact='a').count()
        return context


class BookListView(generic.ListView):
    model = models.Book
    template_name = 'bookcase_app/book_list.html'


class BookDetailView(generic.DetailView):
    model = models.Book
    template_name = 'bookcase_app/book_detail.html'


class AuthorListView(generic.ListView):
    model = models.Author
    template_name = 'bookcase_app/author_list.html'
