# Generated by Django 2.0 on 2019-05-31 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0016_auto_20190531_2136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrow',
            old_name='stock',
            new_name='quantity',
        ),
    ]
