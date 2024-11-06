from django.db import models
from django.contrib.auth.models import AbstractUser

class Manager(AbstractUser):
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.username

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    student_class = models.CharField(max_length=50)  # Tránh sử dụng từ khóa Class
    birthday = models.DateField()
    student_id = models.CharField(max_length=128, unique=True)  # Tránh trùng tên lớp

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    publish_date = models.DateField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class BookTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Đổi thành chữ thường
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Đổi thành chữ thường
    borrow_date = models.DateField(auto_now_add=True)
    days_registered = models.PositiveIntegerField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Transaction {self.id} - {self.student.name} - {self.book.title}"

class LibraryLog(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Đổi thành chữ thường
    checked_in = models.DateTimeField()
    checked_out = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Log {self.id} - {self.student.name}"
