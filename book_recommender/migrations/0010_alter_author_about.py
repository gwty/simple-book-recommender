# Generated by Django 5.1.1 on 2024-09-21 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_recommender', '0009_remove_bookshelf_author_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='about',
            field=models.TextField(default=''),
        ),
    ]
