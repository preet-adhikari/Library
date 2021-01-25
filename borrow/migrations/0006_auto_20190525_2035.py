# Generated by Django 2.0 on 2019-05-25 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0005_remove_borrow_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrow',
            old_name='inventory',
            new_name='cart',
        ),
        migrations.AddField(
            model_name='borrow',
            name='book_code',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
