from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def is_posititve(value):
    if value<0:
        raise ValidationError("the value you have entered is negative")

class BookCategory(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Book(models.Model):
    book_name = models.CharField(max_length=20,unique=True)
    pur_date = models.DateField()
    available = models.IntegerField(validators=[is_posititve],default=1)
    stock = models.IntegerField(validators=[is_posititve],default=1)
    category = models.ForeignKey(BookCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name



