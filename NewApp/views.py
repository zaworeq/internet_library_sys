import datetime
from dateutil.parser import parse
import json

from django.shortcuts import render
from django.views.generic import ListView
import requests
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


from .models import Book
from .forms import NewBookForm, ImportForm
from .serializers import BookListSerializer


def home(request):
    return render(request, 'home_page.html', {})


class BookList(ListView):
    model = Book
    template_name = 'book_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = ''

        if (Book.objects.filter(title__icontains=query)):
            return Book.objects.filter(title__icontains=query)
        elif (Book.objects.filter(author__icontains=query)):
            return Book.objects.filter(author__icontains=query)
        elif (Book.objects.filter(publication_language__icontains=query)):
            return Book.objects.filter(publication_language__icontains=query)
        else:
            return Book.objects.all()


def new_book(request):
    form = NewBookForm()

    if request.method == 'POST':
        form = NewBookForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'new_book.html', context)


def import_(request):
    api_url = 'https://www.googleapis.com/books/v1/volumes?q=Hobbit'
    response = requests.get(api_url)
    input_dict = response.json()
    for book in input_dict['items']:
        try:
            if (isinstance(book['volumeInfo']['industryIdentifiers'][0]['identifier'], int) == True):
                b = Book(title=book['volumeInfo']['title'],
                         author=book['volumeInfo']['authors'][0],
                         publication_date=parse(book['volumeInfo']['publishedDate']).date(),
                         isbn_number=book['volumeInfo']['industryIdentifiers'][0]['identifier'],
                         page_number=book['volumeInfo']['pageCount'],
                         front_page_url=book['volumeInfo']['previewLink'],
                         publication_language=book['volumeInfo']['language'])
            else:
                isbn_str = str(book['volumeInfo']['industryIdentifiers'][0]['identifier'])
                isbn = int(isbn_str[4:])
                b = Book(title=book['volumeInfo']['title'],
                         author=book['volumeInfo']['authors'][0],
                         publication_date=parse(book['volumeInfo']['publishedDate']).date(),
                         isbn_number=isbn,
                         page_number=book['volumeInfo']['pageCount'],
                         front_page_url=book['volumeInfo']['previewLink'],
                         publication_language=book['volumeInfo']['language'])
        except KeyError:
            isbn_str = str(book['volumeInfo']['industryIdentifiers'][0]['identifier'])
            isbn = int(isbn_str[4:])
            b = Book(title=book['volumeInfo']['title'],
                     author=book['volumeInfo']['authors'][0],
                     publication_date=parse(book['volumeInfo']['publishedDate']).date(),
                     isbn_number=isbn,
                     front_page_url=book['volumeInfo']['previewLink'],
                     publication_language=book['volumeInfo']['language'])

        b.save()

        print(b)
    context = {}
    return render(request, 'import.html', context)


class BookListREST(ListAPIView):
    search_fields = ['title',
                     'author',
                     'publication_date',
                     'isbn_number',
                     'page_number',
                     'front_page_url',
                     'publication_language']
    filterset_fields = ['title',
                        'author',
                        'publication_date',
                        'isbn_number',
                        'page_number',
                        'publication_language']
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


