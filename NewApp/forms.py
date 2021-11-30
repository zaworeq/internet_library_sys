from django.forms import ModelForm
from .models import Book


class NewBookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class ImportForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
