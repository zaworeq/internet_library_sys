from django.contrib import admin
from django.urls import path

from NewApp.views import BookList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book_list/', BookList.as_view())
]
