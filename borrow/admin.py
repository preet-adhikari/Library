from django.contrib import admin
from .models import Borrow,BorrowStatus

# Register your models here.
admin.site.register(Borrow)
admin.site.register(BorrowStatus)
