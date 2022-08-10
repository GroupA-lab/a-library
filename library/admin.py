from django.contrib import admin
from . models import Book, IssuedBook, Student

admin.site.register(Book)
admin.site.register(IssuedBook)
admin.site.register(Student)

