from rest_framework import serializers
from .models import Manager, Student, Book, BookTransaction, LibraryLog
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'username', 'password']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTransaction
        fields = '__all__'

class LibraryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryLog
        fields = '__all__'
