from django.utils.text import slugify

from general.models import AbstractEntity
from django.db import models
from authors.models import Author
from django.contrib.auth.models import User


class Genre(AbstractEntity):
    genreName = models.CharField(max_length=30, default="None")
    slug = models.CharField(max_length=30, default="None")

    def __str__(self):
        return self.genreName

class BookManager(models.Manager):
    def create_book(
            self,
            title,
            description,
            author,
            genre,
    ):
        book_slug = slugify(title)
        book = self.create(
            title=title,
            description=description,
            pages=2,
            rating=0,
            slug=book_slug
        )
        book.authors.set([author])
        book.genre.set([genre])
        return book

class Book(AbstractEntity):
    objects = BookManager()

    STATUS = (
        ("P", "Pending"),
        ("A", "Accepted"),
        ("R", "Rejected")
    )
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=50, default="None")
    description = models.TextField(default="None")
    genre = models.ManyToManyField(Genre)
    rating = models.FloatField(default=None)
    pages = models.IntegerField(default=None)
    slug = models.SlugField()
    publishDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=10, default="P")


    def __str__(self):
        return self.title

    def snippet(self):
        return self.description[:50] + '...'


class FavoriteBooks(AbstractEntity):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ReviewManager(models.Manager):
    def create_review(
            self,
            vote,
            review,
            book,
            user
    ):
        return self.create(
            vote = vote,
            review = review,
            book = book,
            user = user
        )

class Review(AbstractEntity):
    STATUS_PENDING = 0
    STATUS_REJECTED = 1
    STATUS_ACCEPTED = 2
    objects = ReviewManager()

    vote = models.IntegerField()
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=30, default="None")
    status = models.IntegerField(default=STATUS_PENDING)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
# Optional

class Series(AbstractEntity):
    name = models.CharField(max_length=30, default="None")
    authors = models.ManyToManyField(Author)
    book = models.ManyToManyField(Book)
    description = models.TextField(default="None")
    rating = models.FloatField(default=None)

