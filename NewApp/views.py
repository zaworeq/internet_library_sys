import json

from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect
import requests

from .models import Book
from .forms import NewBookForm, ImportForm


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


def import_():
    api_url = 'https://www.googleapis.com/books/v1/volumes?q=Hobbit'
    response = requests.get(api_url)
    input_dict = response.json()
    output_dict = [{k: v for k, v in input_dict.items() if k in ["title",
                                                        "authors",
                                                        "publishedDate",
                                                        "identifier",
                                                        "pageCount",
                                                        "previewLink",
                                                        "language"]
                    } for x in input_dict]

    print(output_dict)
    context = {}
    # return render(request, 'import.html', context)
