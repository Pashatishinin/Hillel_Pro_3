import os

from django.urls import path

from . import views


app_name = 'catalog'
urlpatterns = [
    path('books/', views.books, name="books"),
    path('authors', views.authors, name="authors"),
    path('publishers', views.publishers, name="publishers"),
    path('stores', views.stores, name="stores"),
    path('', views.index, name="index"),

    path('author/<int:book_id>/', views.author_detail, name='author_detail'),

    path('books/<int:book_id>/', views.book_detail, name='book_detail'),

    path('publisher/<int:book_id>/', views.publisher_detail, name='publisher-detail'),

path('store/<int:book_id>/', views.store_detail, name='store-detail'),
]