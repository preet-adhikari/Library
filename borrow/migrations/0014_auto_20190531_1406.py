# Generated by Django 2.0 on 2019-05-31 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0013_auto_20190530_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='book_code',
            field=models.IntegerField(default='1'),
        ),
    ]
