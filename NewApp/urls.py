from django.urls import path
from . import views

from NewApp.views import BookList, BookListREST

urlpatterns = [
    path('', views.home, name='home'),
    path('book_list/', BookList.as_view()),
    path('new_book/', views.new_book, name='new book'),
    path('import/', views.import_, name='import'),
    path('api/', BookListREST.as_view()),

]
