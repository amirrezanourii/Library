#from django.urlconf.urls import url
from . import views
from django.urls import path



app_name = 'bookcase_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('book_list/', views.BookList.as_view(), name='book_list'),
    path('book_detail/', views.BookDetailView.as_view(), name='book_detail')

]