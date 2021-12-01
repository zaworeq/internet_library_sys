from django.test import TestCase

from .models import Book


class BasicTest(TestCase):
    def setUp(self):
        self.book = Book()
        self.book.title = 'Test'
        self.book.author = 'TestAuthor'
        self.book.publication_date = '2000-09-24 01:20'
        self.book.publication_language = 'pl'
        self.book.save()

    def test_fields(self):
        book = Book()
        book.title = 'Test'
        book.author = 'TestAuthor'
        book.publication_date = '2000-09-24 01:20'
        book.publication_language = 'pl'
        book.save()

        record = Book.objects.get(pk=book.pk)
        self.assertEqual(record, book)




