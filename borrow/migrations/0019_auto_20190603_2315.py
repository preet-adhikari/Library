# Generated by Django 2.0 on 2019-06-03 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0018_auto_20190603_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='return_date',
            field=models.DateField(),
        ),
    ]
