from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=20,default=1)
    last_name = models.CharField(max_length=20,default=2)
    department = models.CharField(max_length=20)
    year = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name