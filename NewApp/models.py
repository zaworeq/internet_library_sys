import datetime
from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateTimeField('publication date')
    isbn_number = models.IntegerField(default=0)
    page_number = models.IntegerField(default=0)
    front_page_url = models.URLField(default='http://www.google.com')
    publication_language = models.CharField(max_length=100)

    def __str__(self):
        return self.title
