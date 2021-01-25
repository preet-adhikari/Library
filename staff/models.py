from django.db import models
# Create your models here.
class Staff(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    department = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

