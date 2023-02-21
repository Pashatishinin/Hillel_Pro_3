from django.shortcuts import render
from django.db import models
from django.db.models import Count, Avg

# Create your views here.
from .models import Author, Book, Publisher, Store



def index(request):

    num_authors = Author.objects.all().count()
    num_books = Book.objects.all().count()
    num_publishers = Publisher.objects.all().count()
    num_stores = Store.objects.all().count()

    rating_middle = Book.objects.aggregate(rating_middle=Avg('rating', output_field=models.FloatField()))
    middle_number = round(rating_middle['rating_middle'],2)
    return render(request, 'index.html', {"num_authors": num_authors, "num_books": num_books,
                                          "num_publishers": num_publishers, "num_stores": num_stores,
                                          "rating_middle": middle_number})


def authors(request):
    data = Author.objects.all()


    return render(request, 'authors.html', {"data": data})


def books(request):
    data = Book.objects.all()

    return render(request, 'books.html', {"data": data})


def publishers(request):
    data = Publisher.objects.all()

    return render(request, 'publishers.html', {"data": data})


def stores(request):
    data = Store.objects.all()
    print("NEW ______________________")
    print(Store.objects.prefetch_related("books"))


    return render(request, 'stores.html', {"data": data})


def author_detail(request, book_id):
    book_list = []
    data = Author.objects.filter(id=book_id)
    for s in Author.objects.prefetch_related('book_set').filter(id=book_id):
        for d in s.book_set.all():
            book_list.append(d)
    select_author = Author.objects.annotate(Count("book")).get(pk=book_id)
    book_counter = select_author.book__count
    return render(request, 'author-detail.html', {"book_list": book_list, "data": data, "book_counter": book_counter})


def book_detail(request, book_id):
    data = Book.objects.filter(id=book_id)
    for s in Book.objects.prefetch_related('authors').filter(id=book_id):
        for d in s.authors.all():
            author_name = d
    return render(request, 'book_detail.html', {"author_name": author_name, "data": data})


def publisher_detail(request, book_id):
    data = Publisher.objects.filter(id=book_id)
    for i in Publisher.objects.prefetch_related("book_set").filter(id=book_id):
        for g in i.book_set.all():
            book_name = g
    return render(request, 'publisher-detail.html', {"book_name": book_name, "data": data})


def store_detail(request, book_id):
    book_list = []
    data = Store.objects.filter(id=book_id)
    for s in Store.objects.prefetch_related('books').filter(id=book_id):
        for d in s.books.all():
            book_list.append(d)
    return render(request, 'store-detail.html', {"book_list": book_list, "data": data})
