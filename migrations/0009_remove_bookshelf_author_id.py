# Generated by Django 5.1.1 on 2024-09-21 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_recommender', '0008_remove_favoritebooks_author_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookshelf',
            name='author_id',
        ),
    ]
