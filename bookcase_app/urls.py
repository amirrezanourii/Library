from . import views
from django.urls import path, re_path, reverse


app_name = 'bookcase_app'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    #re_path(r'^book/(?P<pk>\d+)/$', views.BookDetailView.as_view(), name='book_detail'),
    path('author_list/', views.AuthorListView.as_view(), name='author_list'),

]
