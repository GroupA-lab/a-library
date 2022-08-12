from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta
 
class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
 
    def __str__(self):
        return str(self.name) + " ["+str(self.isbn)+']'
 
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classroom = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=3, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to="", blank=True)
 
    def __str__(self):
        return str(self.user) + " ["+str(self.branch)+']' + " ["+str(self.classroom)+']' + " ["+str(self.roll_no)+']'
 
def expiry():
    return datetime.today() + timedelta(days=14)
    
class IssuedBook(models.Model):
    student_id = models.CharField(max_length=100, blank=True) 
    isbn = models.CharField(max_length=13)
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)

#def borrow_book_view(request, std_number, bk_id ):
 #   notify()
  #  book_being_borrowed = Books.objects.get( id = bk_id )
   # borrowing_student = Std_model.objects.get( personal_No = std_number)
    #if (not book_being_borrowed.availability):
     #   return HttpResponse("<h1>Book already Booked or reserved</h1>")
    #else:
     #   try:
      #      Borrowedbooks(bks_id = book_being_borrowed, std_number = borrowing_student, borrow_date = dt.datetime.now().date()).save()
       #     try:
        #        book_being_borrowed.availability = False
         #       book_being_borrowed.save()
          #      Borrowedbooks(bks_id = book_being_borrowed, std_number = borrowing_student, borrow_date = dt.datetime.now().date()).save()
           # except:
            #    pass
            #return HttpResponse(f"<h1>You have succeesfully borrowed {book_being_borrowed.book_title}</h1>")
        #except:
         #   return HttpResponse("<h1>One can only borrow one book at time</h1>")