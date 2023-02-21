from django.contrib import admin

from .models import Book, Author, Publisher, Store


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'pubdate')
    fieldsets = (
        (None, {'fields': ['name']}),
        (None, {'fields': ['authors']}),
        (None, {'fields': ['pages', 'rating', 'price']}),
        ("PUBLISHER", {'fields': ['publisher']}),
        ('DATE INFORMATION', {'fields': ['pubdate'], 'classes': ['collapse']}))
    filter_horizontal = ['authors']
    search_fields = ['name']
    date_hierarchy = 'pubdate'
    list_filter = ['rating']



@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [BookInline]


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    search_fields = ['name']
    filter_horizontal = ['books']


