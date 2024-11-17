from django.forms import ValidationError
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
import random, string
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
def generate_book_id():
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"book_{random_part}"
class Manager(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now, editable=False) 
    updated_at = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.username

class Student(models.Model):#checked
    id = models.CharField(primary_key=True, max_length=8, default=generate_random_string, editable=False, unique=True)
    name = models.CharField(max_length=255)
    student_class = models.CharField(max_length=50)  # Tránh sử dụng từ khóa Class
    birthday = models.DateField()
    student_id = models.CharField(max_length=128, unique=True)  # Tránh trùng tên lớp
    created_at = models.DateTimeField(default=timezone.now, editable=False) 
    updated_at = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.CharField(
        primary_key=True, 
        max_length=9,  # "book_" + 4 ký tự = 9 ký tự
        default=generate_book_id, 
        editable=False, 
        unique=True
    )
    title = models.CharField(max_length=255, unique= True)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    cover_image = models.CharField(max_length=255, blank=True)
    publish_date = models.DateField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now, editable=False) 
    updated_at = models.DateTimeField(auto_now=True) 
    def save(self, *args, **kwargs):
        if self.quantity <= 0:
            raise ValidationError("This book is currently unavailable.")
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title

class BookTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student,to_field='student_id', on_delete=models.CASCADE)  
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  
    borrow_date = models.DateField(default= timezone.now)
    days_registered = models.PositiveIntegerField()
    return_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)  
    updated_at = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return f"Transaction {self.id} - {self.student.name} - {self.book.title}"

class LibraryLog(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, to_field='student_id',on_delete=models.CASCADE) 
    checked_in = models.DateTimeField(default=timezone.now)
    checked_out = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f"Log {self.id} - {self.student.name}"
class Token(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=255, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False) 
    updated_at = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.token