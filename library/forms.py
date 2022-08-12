from django.forms import ModelForm
from . models import Book, Student, IssuedBook
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class Add_book(ModelForm):
    class Meta:
        model = Book
        exclude = []

class add_student(ModelForm):
    class Meta:
        model = Student
        exclude = []

class IssuedBookForm(ModelForm):
    class Meta:
        model = IssuedBook
        exclude = []

class Add_Student(ModelForm):
    class Meta:
        model = Student
        exclude = []

