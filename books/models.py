from general.models import AbstractEntity
from django.db import models
from authors.models import Author
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(AbstractEntity):
    genreName = models.CharField(max_length=30, default="None")
    slug = models.CharField(max_length=30, default="None")

    def __str__(self):
        return self.genreName


class Book(AbstractEntity):
    STATUS = (
        ("P", "Pending"),
        ("A", "Accepted"),
        ("R", "Rejected")
    )
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=50, default="None")
    description = models.TextField(default="None")
    genre = models.ManyToManyField(Genre)
    rating = models.IntegerField(default=0)
    pages = models.IntegerField(default=None)
    slug = models.SlugField(default="None")
    publishDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=10, default="None")


    def __str__(self):
        return self.title

    def snippet(self):
        return self.description[:50] + '...'


class FavoriteBooks(AbstractEntity):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Review(AbstractEntity):
    vote = models.IntegerField(default=0,
                               validators=[
                                MaxValueValidator(5),
                                MinValueValidator(0),
                               ])
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=30, default="None")
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()

# Optional

class BookRequest(Book):
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class Series(AbstractEntity):
    name = models.CharField(max_length=30, default="None")
    authors = models.ManyToManyField(Author)
    book = models.ManyToManyField(Book)
    description = models.TextField(default="None")
    rating = models.FloatField(default=None)

