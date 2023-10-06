from django.shortcuts import render
from django.http import HttpResponseNotFound, JsonResponse, Http404
from .models import Book


def get_books_views(request):
    all_books = Book.objects.all()
    return render(request, 'books/all_books.html', {'all_books': all_books})
 

def get_book_by_id_views(request, book_id):
    book = Book.objects.filter(id=book_id).first()
    if not book:
        return render(request, 'books/error404.html')
    return render(request, 'books/get_book_by_id.html', {'book': book})


def get_api_books_views(request):
    books = Book.objects.all() 
    books_list = []
    for book in books:
        book_dict = create_json_book(book)
        books_list.append(book_dict)

    return JsonResponse(books_list, safe=False, json_dumps_params={'ensure_ascii': False})


def get_api_books_by_id_views(request, book_id):
    book = Book.objects.filter(id=book_id).first()
    if not book:
        return render(request, 'books/error404.html')
    book_dict = create_json_book(book)
    return JsonResponse([book_dict] , safe=False, json_dumps_params={'ensure_ascii': False})


def create_json_book(book):
    book_dict = {}
    book_dict['id'] = book.id
    book_dict['itle'] = book.title
    book_dict['uthor_full_name'] = book.author_full_name
    book_dict['ear_of_publishing'] = book.year_of_publishing
    book_dict['opies_printed'] = book.copies_printed
    book_dict['short_description'] = book.short_description
    return book_dict