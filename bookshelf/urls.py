from django.contrib import admin
from django.urls import path
from books.views import get_books_views
from books.views import get_book_by_id_views
from books.views import get_api_books_views
from books.views import get_api_books_by_id_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', get_books_views),
    path('books/<int:book_id>/', get_book_by_id_views),
    path('api/books/', get_api_books_views),
    path('api/books/<int:book_id>/', get_api_books_by_id_views),

]
