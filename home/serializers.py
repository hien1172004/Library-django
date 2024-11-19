from rest_framework import serializers
from .models import LibraryLog, Manager, Student, Book, BookTransaction, Category


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'username', 'password']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'student_class', 'birthday', 'student_id']

# Serializer cho Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'category', "cover_image", 'publish_date', 'quantity']

# Serializer cho BookTransaction
class BookTransactionSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    book = BookSerializer(read_only=True)

    class Meta:
        model = BookTransaction
        fields = ['id', 'student', 'book', 'borrow_date', 'days_registered', 'return_date']

    def create(self, validated_data):
        # Tạo một giao dịch mới
        return super().create(validated_data)

# Serializer cho LibraryLog
class LibraryLogSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)

    class Meta:
        model = LibraryLog
        fields = ['id', 'student', 'checked_in', 'checked_out']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'label']
