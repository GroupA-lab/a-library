from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('index/', views.index, name="index"),    
    path('add_book/', views.Add_book_view, name = "add book url" ),
    path('add_student/', views.Add_students_view, name = "add student url" ),
    path("view_books/", views.view_books, name="view_books"),
    path("view_students/", views.view_students, name="view_students"),
    path("issue_book/", views.issue_book, name="issue_book"),
    path("view_issued_book/", views.view_issued_book, name="view_issued_book"),
    path("profile/", views.profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path('register/', views.registeruser, name="register"),
    #path("change_password/", views.change_password, name="change_password"),
    path('login/', views.loginUser, name="login"),
    #path("admin_login/", views.admin_login, name="admin_login"),
    #path("logout/", views.Logout, name="logout"),
 
    #ath("delete_book/<int:myid>/", views.delete_book, name="delete_book"),
    #path("delete_student/<int:myid>/", views.delete_student, name="delete_student"),
]
