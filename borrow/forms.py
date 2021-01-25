from django import forms
from .models import Borrow
from student.models import Student
from book.models import Book
from .models import BorrowStatus


class BorrowForm(forms.ModelForm):
    Student = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=Student.objects.all())
    Book = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=Book.objects.all())
    borrow_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    status = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=BorrowStatus.objects.all())
    book_code = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    #lost = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    class Meta:
        model = Borrow
        fields = ['Student','Book','borrow_date','status','book_code']