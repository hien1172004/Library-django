from django.forms import ValidationError
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
import random, string, time


def generate_random_string():
    random_part = "".join(random.choices(string.ascii_letters + string.digits, k=4))
    return f"student_{random_part}"


def generate_book_id():
    random_part = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"book_{random_part}"


def generate_library():
    random_part = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"lib_{random_part}"


def generate_trans():
    random_part = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"trans_{random_part}"


def generate_category():
    random_part = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"category_{random_part}"


class Manager(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.BigIntegerField(
        editable=False
    )  # Lưu trữ Unix timestamp cho thời gian tạo
    updated_at = models.BigIntegerField(
        editable=False
    )  # Lưu trữ Unix timestamp cho thời gian cập nhật

    def save(self, *args, **kwargs):
        # Chuyển đổi thời gian hiện tại thành Unix timestamp trước khi lưu
        if not self.created_at:
            self.created_at = int(time.time())
        self.updated_at = int(time.time())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Student(models.Model):  # checked
    id = models.CharField(
        primary_key=True,
        max_length=12,
        default=generate_random_string,
        editable=False,
        unique=True,
    )
    name = models.CharField(max_length=255)
    student_class = models.CharField(max_length=50)  # Tránh sử dụng từ khóa Class
    birthday = models.BigIntegerField()
    student_id = models.CharField(max_length=128, unique=True)  # Tránh trùng tên lớp
    created_at = models.BigIntegerField(
        editable=False
    )  # Lưu trữ Unix timestamp cho thời gian tạo
    updated_at = models.BigIntegerField(
        editable=False
    )  # Lưu trữ Unix timestamp cho thời gian cập nhật

    def save(self, *args, **kwargs):
        # Chuyển đổi thời gian hiện tại thành Unix timestamp trước khi lưu
        if not self.created_at:
            self.created_at = int(time.time())
        self.updated_at = int(time.time())  # Cập nhật trường updated_at
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=9,  # "book_" + 4 ký tự = 9 ký tự
        default=generate_book_id,
        editable=False,
        unique=True,
    )
    title = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    cover_image = models.CharField(max_length=255, blank=True)
    publish_date = models.BigIntegerField()
    quantity = models.IntegerField()
    created_at = models.BigIntegerField(
        editable=False
    )  # Lưu trữ Unix timestamp cho thời gian tạo
    updated_at = models.BigIntegerField(
        editable=False
    )  # Lưu trữ Unix timestamp cho thời gian cập nhật

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = int(time.time())
        self.updated_at = int(time.time())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class BookTransaction(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=10,
        default=generate_trans,
        editable=False,
        unique=True,
    )
    student = models.ForeignKey(
        Student, to_field="student_id", on_delete=models.CASCADE
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.BigIntegerField(editable=False)  # Unix timestamp
    days_registered = models.PositiveIntegerField()
    return_date = models.BigIntegerField(
        null=True, blank=True, editable=False
    )  # Unix timestamp
    created_at = models.BigIntegerField(editable=False)  # Unix timestamp
    updated_at = models.BigIntegerField(editable=False)  # Unix timestamp

    def save(self, *args, **kwargs):
        # Nếu borrow_date chưa được set, lấy thời gian hiện tại
        if not self.borrow_date:
            self.borrow_date = int(time.time())

        # Lưu thời gian tạo nếu chưa có
        if not self.created_at:
            self.created_at = int(time.time())

        # Cập nhật thời gian
        self.updated_at = int(time.time())

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Transaction {self.id} - {self.student.name} - {self.book.title}"


class LibraryLog(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=8,
        default=generate_library,
        editable=False,
        unique=True,
    )
    student = models.ForeignKey(
        Student, to_field="student_id", on_delete=models.CASCADE
    )
    checked_in = models.BigIntegerField()  # Unix timestamp cho thời gian mượn
    checked_out = models.BigIntegerField(
        null=True, blank=True
    )  # Unix timestamp cho thời gian trả sách (có thể null)

    def save(self, *args, **kwargs):
        if not self.checked_in:
            self.checked_in = int(time.time())  # Lưu timestamp khi mượn sách

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Log {self.id} - {self.student.name}"


class Category(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=13,
        default=generate_category,
        editable=False,
        unique=True,
    )
    label = models.CharField(max_length=255, unique=True)
    created_at = models.BigIntegerField(
        editable=False
    )  # Lưu trữ Unix timestamp cho thời gian tạo
    updated_at = models.BigIntegerField(
        editable=False
    )  # Lưu trữ Unix timestamp cho thời gian cập nhật

    def save(self, *args, **kwargs):
        # Chuyển đổi thời gian hiện tại thành Unix timestamp trước khi lưu
        if not self.created_at:
            self.created_at = int(time.time())
        self.updated_at = int(time.time())
        super().save(*args, **kwargs)
