from django.forms import ModelForm
from . models import Book, Student, IssuedBook
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

        
class add_book(ModelForm):
    class Meta:
        model = Book
        exclude = []

class add_student(ModelForm):
    class Meta:
        model = Student
        exclude = []

class IssuedBook(ModelForm):
    class Meta:
        model = IssuedBook
        exclude = []



