from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    department = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    year = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))


    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'department','year']


