from django.db import models
from book.models import Book
from student.models import Student
from staff.models import Staff
from datetime import date


# Create your models here.

class BorrowStatus(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status

class Borrow(models.Model):
    Book = models.ForeignKey(Book,on_delete=models.CASCADE,default=1)
    Student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True,blank=True)
    Staff = models.ForeignKey(Staff,on_delete=models.CASCADE,null=True,blank=True)
    book_code = models.IntegerField(default='1')
    quantity = models.IntegerField(default=1)
    status = models.ForeignKey(BorrowStatus,on_delete=models.CASCADE,null=True,blank=True)
    lost = models.TextField(null=True,blank=True)
    borrow_date = models.DateField(default=date.today)
    return_date = models.DateField(null=True,blank=True)










