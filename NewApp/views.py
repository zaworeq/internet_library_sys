from django.shortcuts import render
from django.views.generic import ListView

from .models import Book


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
