from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import *
from django.template import loader
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User



def index(request):
    return render(request, 'index.html', {})

def home(request):
    return render(request, 'home.html', {})


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

def admin_home(request):
    return render(request, "admin_home.html")

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

def registerUser(request):
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

            User = authenticate(username=username, password=password)

            if User is not None:
                login(request, User)
            return redirect('index')
        else:
            messages.error(request, 'Invalid login Bambi.., PLIZ GO BACK AND FIRST REGISTER')
    else:
        messages.error(request, 'Complete the fields')

    return render(request, 'login.html', {})

def Logout(request):
    logout(request)
    return redirect ("index")


def StudentDelete(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    obj.delete()
    return redirect('index')

def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect("/admin_home")
            else:
                return HttpResponse("You are not an admin.")
        else:
            alert = True
            return render(request, "admin_login.html", {'alert':alert})
    return render(request, "admin_login.html")

def borrow_book_view(request, std_number, bk_id ):
    notify()
    book_being_borrowed = Books.objects.get( id = bk_id )
    borrowing_student = Std_model.objects.get( personal_No = std_number)
    if (not book_being_borrowed.availability):
        return HttpResponse("<h1>Book already Booked or reserved</h1>")
    else:
        try:
            Borrowedbooks(bks_id = book_being_borrowed, std_number = borrowing_student, borrow_date = dt.datetime.now().date()).save()
            try:
                book_being_borrowed.availability = False
                book_being_borrowed.save()
                Borrowedbooks(bks_id = book_being_borrowed, std_number = borrowing_student, borrow_date = dt.datetime.now().date()).save()
            except:
                pass
            return HttpResponse(f"<h1>You have succeesfully borrowed {book_being_borrowed.book_title}</h1>")
        except:
            return HttpResponse("<h1>One can only borrow one book at time</h1>")