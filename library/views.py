from django.shortcuts import render,redirect
from book.forms import BookForm
from student.forms import StudentForm
from staff.forms import StaffForm
from borrow.forms import BorrowForm
from django.db.models import F
from book.models import Book
from student.models import Student
from borrow.models import Borrow,BorrowStatus
from datetime import datetime
from django.contrib.auth import authenticate



def book(request):
    if request.method=="GET":
        books = Book.objects.all()
        context = {
            'form': BookForm,'book1':books
        }
        return render(request,'book.html',context)

    else:
        form = BookForm(request.POST)
        if form.is_valid():
            data = form.save()
            data.save()
            return redirect('book')
        return render(request,'book.html')

def add_book(request,id):
    if request.method=="GET":
        books = Book.objects.get(id=id)
        form = BookForm(instance=books)
        context = {
            'form': form
        }
        return render(request, 'add_book.html', context)
    else:
        i = int(request.POST.get("includeid"))
        form = BookForm(request.POST,id)
        books = Book.objects.get(id=id)
        books.available = F('available')+i
        books.stock = F('stock')+i
        books.save()
        if form.is_valid():
            form.save()
            return redirect('book')
        return render(request, 'book.html')

def delete_item(request,id):
    books = Book.objects.get(id=id)
    books.delete()
    return redirect('book')


def student(request):
    if request.method=='GET':
        students = Student.objects.all()
        context={
            'form': StudentForm,'std': students
        }
        return render(request,'student.html',context)

    else:
        form = StudentForm(request.POST)
        if form.is_valid():
            data = form.save()
            data.save()
            return redirect('student')

        return render(request,'student.html')

def staff(request):
    if request.method=='GET':
        context={
            'form': StaffForm
        }
        return render(request,'staff.html',context)

    else:
        form = StaffForm(request.POST)
        if form.is_valid():
            data = form.save()
            data.save()
            return redirect('staff')

        return render(request,'staff.html')

def borrow(request):
    borrows = Borrow.objects.all()
    books = Book.objects.all()
    context = {
        'form':BorrowForm,'borrow1':borrows,'book1':books
    }
    if request.method == 'GET':
        return render(request,'borrow.html',context)

    else:
        form = BorrowForm(request.POST)
        b = int(request.POST.get('Book'))
        x = Book.objects.get(id=b)
        y = x.available
        if form.is_valid():
            b = request.POST.get('status')
            if b == str(1):
                if y > 0:
                    x.available = F('available') - 1
                    x.save()
                else:
                    return render(request, 'borrow.html', {'alert': 'Book not available'})

                data = form.save()
                data.save()
                return redirect('borrow')


        return render(request,'borrow.html')

def return1(request):
    borrows = Borrow.objects.all()
    books = Book.objects.all()
    context = {
        'form': BorrowForm, 'borrow1': borrows, 'book1': books
    }
    if request.method=='GET':
        return render(request,'return1.html',context)

    else:
        b = int(request.POST.get('borrow_id'))
        x = Borrow.objects.get(id = b)
        x.return_date = datetime.now()
        if x.status != BorrowStatus.objects.get(id = 3):
            x.status = BorrowStatus.objects.get(id=3)
            x.Book.available = (int(x.Book.available)) + 1
            x.Book.save()
            x.save()
            return redirect('borrow')
        else:
            x.save()
            return redirect('borrow')

def lost(request):
    borrows = Borrow.objects.all()
    books = Book.objects.all()
    context = {
        'form': BorrowForm, 'borrow1': borrows, 'book1': books
    }
    if request.method == 'GET':
        return render(request, 'lost.html', context)

    else:
        b = int(request.POST.get('borrow_id'))
        d = str(request.POST.get('text_id'))
        x = Borrow.objects.get(id=b)
        x.lost = d
        x.return_date = datetime.now()
        if x.status != BorrowStatus.objects.get(id=3) and x.status != BorrowStatus.objects.get(id=2) :
            x.status = BorrowStatus.objects.get(id=2)
            x.Book.stock = (int(x.Book.stock)) - 1
            x.Book.save()
            x.save()
            return redirect('borrow')
        else:
            x.save()
            return redirect('borrow')


def update1():
    books = Book.objects.get(id=id)
    books.available = F('available') + 1

def update2():
    books = Book.objects.get(id=id)
    books.available = F('available') - 1

def update3():
    books = Book.objects.get(id=id)
    books.stock = F('stock') - 1













