from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView, DetailView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from .forms import RenewBookForm


# (functional views)
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


class LoanedBookByUser(LoginRequiredMixin, generic.ListView):
    model = models.BookInstance
    template_name = 'bookcase_app/books_loaned_by_user.html'
    paginate_by = 5

    def get_queryset(self):
        return models.BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('return_back_day')



def renew_book_librarian(request, pk):

    book_inst = get_object_or_404(models.BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_inst.return_back_day = form.cleaned_data['renew_date']
            book_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('bookcase_app:mybooks'))

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renew_date': proposed_renewal_date, })

    return render(request, 'bookcase_app/book_renew_librarian.html', {'form': form, 'bookinst': book_inst})
    