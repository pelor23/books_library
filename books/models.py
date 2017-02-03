from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name="Imię:")
    surname = models.CharField(max_length=200, verbose_name="Nazwisko:")
    # written_books = models.ForeignKey(Book, verbose_name="Napisane książki:")


class BookCategory(models.Model):
    pass


class Publisher(models.Model):
    pass


class CoverType(models.Model):
    pass


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tytuł:")
    subtitle = models.CharField(max_length=200, verbose_name="Podtytuł:", blank=True)
    authors = models.ManyToManyField(Author, verbose_name="Autorzy:")
    pub_year = models.IntegerField(max_length=5, verbose_name="Rok wydania:")
    which_edition = models.CharField(max_length=3, verbose_name="Które wydanie:", blank=True)
    publisher = models.ForeignKey(Publisher, verbose_name="Wydawca/Wydawnictwo:")
    pub_place = models.CharField(max_length=200, verbose_name="Miasto:")
    category = models.ForeignKey(BookCategory, verbose_name="Kategoria:")
    pages = models.IntegerField(max_length=4, verbose_name="Ilość stron:")
    cover_type = models.ForeignKey(CoverType, verbose_name="Typ okładki:")
    # isbn
