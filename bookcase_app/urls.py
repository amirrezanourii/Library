#from django.urlconf.urls import url
from . import views

app_name = 'bookcase_app'
urlpatterns = [
    path('', views.Index(), name='index'),
    
]