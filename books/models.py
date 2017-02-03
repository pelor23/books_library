from django.db import models


class Author(object):
    pass


class BookCategory(object):
    pass


class Publisher(object):
    pass


class CoverType(object):
    pass


class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    authors = models.ForeignKey(Author)
    pub_year = models.IntegerField(max_length=5)
    which_edition = models.CharField(max_length=3)
    publisher = models.ForeignKey(Publisher)
    pub_place = models.CharField(max_length=200)
    category = models.ForeignKey(BookCategory)
    pages = models.IntegerField(max_length=4)
    cover_type = models.ForeignKey(CoverType)
    # isbn

