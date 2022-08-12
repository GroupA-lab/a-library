from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import *
from django.template import loader
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return render(request, 'home.html', {})

def index(request):
    return render(request, 'index.html', {})

def Add_book_view(request):
    form = Add_book(request.POST or None)
    if form.is_valid():
        form.save()
        form = Add_book(request.POST)
    context = {
        "form" : form
     }
    return render(request,"add_book.html",context)

def view_books(request):
    books = Book.objects.all()
    return render(request, "view_books.html", {'books':books})

def view_students(request):
    students = Student.objects.all()
    return render(request, "view_students.html", {'students':students})

def issue_book(request):
    form = IssuedBookForm()
    if request.method == "POST":
        form = IssuedBookForm(request.POST)
        if form.is_valid():
            obj = models.IssuedBook()
            obj.student_id = request.POST['name2']
            obj.isbn = request.POST['isbn2']
            obj.save()
            alert = True
            return render(request, "issue_book.html", {'obj':obj, 'alert':alert})
    return render(request, "issue_book.html", {'form':form})

def view_issued_book(request):
    issuedBooks = IssuedBook.objects.all()
    details = []
    for i in issuedBooks:
        days = (date.today()-i.issued_date)
        d=days.days
        fine=0
        if d>14:
            day=d-14
            fine=day*5
        books = list(models.Book.objects.filter(isbn=i.isbn))
        students = list(models.Student.objects.filter(user=i.student_id))
        i=0
        for l in books:
            t=(students[i].user,students[i].user_id,books[i].name,books[i].isbn,issuedBooks[0].issued_date,issuedBooks[0].expiry_date,fine)
            i=i+1
            details.append(t)
    return render(request, "view_issued_book.html", {'issuedBooks':issuedBooks, 'details':details})

def profile(request):
    return render(request, "profile.html")

def edit_profile(request):
    student = Student.objects.get(user=request.user.id)
    if request.method == "POST":
        email = request.POST['email']
        phone = request.POST['phone']
        branch = request.POST['branch']
        classroom = request.POST['classroom']
        roll_no = request.POST['roll_no']
 
        student.user.email = email
        student.phone = phone
        student.branch = branch
        student.classroom = classroom
        student.roll_no = roll_no
        student.user.save()
        student.save()
        alert = True
        return render(request, "edit_profile.html", {'alert':alert})
    return render(request, "edit_profile.html")

def Add_students_view(request):
    form = Add_Student(request.POST or None)
    if form.is_valid():
        form.save()
        form = Add_Student()
    context = {
        "form" : form
    }
    return render(request,"add_student.html",context)

def registeruser(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form':form})

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login Bambi.., PLIZ GO BACK AND FIRST REGISTER')
    else:
        messages.error(request, 'Complete the fields')

    return render(request, 'login.html', {})

def logoutUser(request):
    logout(request)
    return redirect('home')


def StudentDelete(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    obj.delete()
    return redirect('index')