# Generated by Django 2.0 on 2019-05-31 16:00

import book.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_remove_book_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='stock',
            field=models.IntegerField(default=1, validators=[book.models.is_posititve]),
        ),
    ]
