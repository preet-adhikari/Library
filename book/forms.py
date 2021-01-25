from django import forms
from .models import Book,BookCategory

class BookForm(forms.ModelForm):
    book_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    available = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    stock = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    pur_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=BookCategory.objects.all())

    class Meta:
        model = Book
        fields = ['book_name','available','stock','pur_date','category']


