from rest_framework.authtoken.models import Token
from rest_framework import viewsets, generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Manager, Student, Book, BookTransaction, LibraryLog
from .serializers import ManagerSerializer, StudentSerializer, BookSerializer, BookTransactionSerializer, LibraryLogSerializer, LoginSerializer
from django.contrib.auth import authenticate
class BookAddAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookSearchAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        title = request.query_params.get("title", None)
        author = request.query_params.get('author', None)
        category = request.query_params.get('category', None)
        page_size = request.query_params.get('pageSize', 10)

        queryset = self.get_queryset()
        if title:
            queryset = queryset.filter(title__icontains=title)
        if author: 
            queryset = queryset.filter(author__icontains=author)
        if category:
            queryset = queryset.filter(category__icontains=category)

        # Phân trang
        paginator = PageNumberPagination()
        paginator.page_size = page_size
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.get_serializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class BookDeleteAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()

    def destroy(self, request, *args, **kwargs):
        book = self.get_object()
        # Kiểm tra xem sách có đã được mượn hay không
        if BookTransaction.objects.filter(book=book).exists():
            return Response({"error": "Cannot delete book that is currently borrowed."}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(book)
        return Response(status=status.HTTP_204_NO_CONTENT)
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer  # Sử dụng LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Kiểm tra tính hợp lệ của dữ liệu
        
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        # Xác thực người dùng
        user = authenticate(username=username, password=password)
        if user is not None:
            # Nếu người dùng xác thực thành công, tạo token
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)