from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.CharField(max_length=255, blank=True)

class FavoriteBooks(models.Model):
    user_id = models.IntegerField()
    book_id = models.IntegerField()

# This is the string representation of the object
    def __str__(self):
        return self.title
        
class Author(models.Model):
    author_id = models.IntegerField()
    name = models.TextField()
    about = models.TextField(blank=True, default='')
    fans_count = models.IntegerField(blank=True, default='')
    image_url = models.TextField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    data_source = models.TextField(blank=True, default='')
    class Meta:
        indexes = [
            models.Index(fields=['author_id'], name='author_id_idx'),
            models.Index(fields=['name'], name='name_idx'),
        ]
        unique_together = ('author_id', 'name',)

class Book(models.Model):
    book_id = models.IntegerField()
    author_id = models.IntegerField(default=-1)
    author_name = models.CharField(max_length=500, blank=True, default='')
    title = models.CharField(max_length=500, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    isbn = models.CharField(max_length=100, blank=True, default='')
    isbn13 = models.CharField(max_length=100, blank=True, default='')
    ratings_count = models.IntegerField(blank=True, default=0)
    description = models.TextField(blank=True, default='')
    average_rating =  models.FloatField(default=0)
    class Meta:
        indexes = [
            models.Index(fields=['description'], name='description_idx'),
            models.Index(fields=['book_id'], name='book_id_idx'),
            models.Index(fields=['title'], name='title_idx'),
            models.Index(fields=['author_name'], name='author_name_idx'),
        ]
        unique_together = ('book_id', 'title',)

class BookShelf(models.Model):
    book_id = models.IntegerField()
    shelf_name = models.CharField(max_length=100, blank=True, default='')
    shelf_count = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['book_id']
        indexes = [
            models.Index(fields=['book_id'], name='book_id_idx2'),
            models.Index(fields=['shelf_name'], name='shelf_name_idx'),
        ]
        unique_together = ('book_id', 'shelf_name','shelf_count')
