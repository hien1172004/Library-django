from django.forms import ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.db.models import F
#----- Phan Trang------
class CustomPageNumberPagination(PageNumberPagination):
    page_size = 2  # Số sách mặc định mỗi trang
    page_size_query_param = 'page_size'  # Cho phép người dùng thay đổi số lượng sách mỗi trang qua tham số page_size
    max_page_size = 10  # Giới hạn số sách tối đa mỗi trang
# --BOOK---
class AddBookView(generics.CreateAPIView):#checked
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Book added successfully!',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'message': 'Failed to add book',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
class EditBookView(generics.UpdateAPIView):#checked
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        
        book_id = self.request.data.get('id')
        if not book_id:
            raise serializers.ValidationError({"id": "Book ID is required"})
        return get_object_or_404(Book, id=book_id)

    def update(self, request, *args, **kwargs):
        book = self.get_object()
        serializer = self.get_serializer(book, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Book updated successfully!',
                'data': serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            'message': 'Failed to update book',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
class SearchBooksView(generics.ListAPIView):#checked
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination
    # permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)  # Sử dụng phương thức `list` của `ListAPIView`
    def get_queryset(self):
        # Lấy các tham số từ query params (tham số trong URL)
        title = self.request.data.get("title", "")
        author = self.request.data.get("author", "")
        category = self.request.data.get("category", "")
        
        queryset = Book.objects.all()
        
        # Áp dụng các bộ lọc nếu có tham số tìm kiếm
        if title:
            queryset = queryset.filter(title__icontains=title)  # Tìm theo tiêu đề sách
        if author:
            queryset = queryset.filter(author__icontains=author)  # Tìm theo tác giả
        if category:
            queryset = queryset.filter(category__icontains=category)  # Tìm theo thể loại sách

        return queryset
class DeleteBookView(generics.DestroyAPIView):#checked
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        # Lấy book_id từ tham số truy vấn
        book_id = self.request.query_params.get('id')
        # Kiểm tra nếu book_id không có trong query params
        if not book_id:
            raise ValidationError('Book id is required.')
        
        # Tìm kiếm sách theo book_id
        return get_object_or_404(Book, id=book_id)

    def delete(self, request, *args, **kwargs):
        book = self.get_object()

        # Kiểm tra nếu sách đã được mượn (ví dụ: quantity == 0)
        if BookTransaction.objects.filter(book=book, return_date__isnull=True).exists():
            return Response({
                'message': 'Book cannot be deleted because it has been borrowed.'
            }, status=status.HTTP_400_BAD_REQUEST)
        book.delete()
        return Response({
            'message': 'Book deleted successfully!'
        }, status=status.HTTP_200_OK)

#--------Manager----------
class LoginView(APIView):#checked
    permission_classes = [AllowAny]  # Cho phép tất cả người dùng gọi API này
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        # Kiểm tra thông tin người dùng
        user = authenticate(username=username, password=password)
        if user is not None:
            # Nếu người dùng hợp lệ, tạo token
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            token = Token.objects.create(token=access_token)
            return Response({
                'access': access_token,  # Trả về token truy cập (access token)
                'refresh': str(refresh),  # Trả về token làm mới (refresh token) - tùy chọn nhưng khuyến khích
            }, status=status.HTTP_200_OK)  # Trả về mã trạng thái 200 (thành công)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
class ChangePasswordView(APIView):#checked
    permission_classes = [IsAuthenticated]  # Chỉ người dùng đã đăng nhập mới có quyền thay đổi mật khẩu

    def post(self, request, *args, **kwargs):
        user = request.user  # Lấy thông tin người dùng đã xác thực
        old_password = request.data.get('old')
        new_password = request.data.get('new')

        # Kiểm tra mật khẩu cũ
        if not user.check_password(old_password):
            return Response({'error': 'Old password is incorrect'}, status=400)

        # Đổi mật khẩu
        user.set_password(new_password)
        user.save()
        return Response({'message': 'Password updated successfully'})
#----------------Students----------
class StudentDetailView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_object(self):
        # Lấy student_id từ query parameter
        student_id = self.request.query_params.get('student_id')
        
        # Kiểm tra nếu student_id không tồn tại trong query parameters
        if not student_id:
            # Trả về phản hồi lỗi nếu không có student_id
            raise ValidationError({
                'message': 'student_id query parameter is required.'
            })
        # Sử dụng get_object_or_404 để tìm Student hoặc trả về 404 nếu không tìm thấy
        return get_object_or_404(Student, student_id=student_id)
class StudentAddView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        serializers = StudentSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({
                'message': 'Student added sucessfully!',
                'data': serializers.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": 'Failed to add student',
            'errors' : serializers.errors
        }, status= status.HTTP_400_BAD_REQUEST)
class StudentEditView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        student_id = self.request.data.get("student_id")
        if not student_id:
            raise ValidationError({"message": "Student_id is requierd"})
        return get_object_or_404(Student,student_id = student_id)
    def update(self, request, *args, **kwargs):
        student = self.get_object()
        serializers = StudentSerializer(student, data = request.data, partial = True)
        if serializers.is_valid():
            serializers.save()
            return Response({
                'message':"student update Success",
                'data' : serializers.data
            }, status= status.HTTP_200_OK)
        return Response({
            'errors': "Failed to update student",
            'data': serializers.errors
        },status= status.HTTP_400_BAD_REQUEST)
class StudentDeleteView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated]
    def get_object(self):
        student_id = self.request.query_params.get('student_id')
        if not student_id:
            raise ValidationError({
                'message': 'student_id query parameter is required.'
            })
        return get_object_or_404(Student, student_id=student_id)
    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        student.delete()
        return Response({'message': 'Delete Successfully'}, status= status.HTTP_204_NO_CONTENT_OK)
class StudentSearchView(generics.ListAPIView):
    serializer_class = StudentSerializer
    pagination_class = PageNumberPagination
    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)  # Sử dụng phương thức `list` của `ListAPIView`
    def get_queryset(self):
        queryset = Student.objects.all()
        name = self.request.data.get("name", "")
        student_class = self.request.data.get("student_class","")  

        if name:
            queryset = queryset.filter(name__icontains=name) 
        if student_class:
            queryset = queryset.filter(student_class__icontains=student_class)  

        return queryset
#--------- LibraryLog-----
class CheckInView(generics.CreateAPIView):
    seriaizer_class= LibraryLogSerializer
    def create(self, request, *args, **kwargs):
        student_id = request.data.get('student_id')
        try:
            student = Student.objects.get(student_id=student_id)
        except Student.DoesNotExist:
            raise ValidationError({"student_id": "Student with this ID does not exist."}) 
        log = LibraryLog.objects.create(student=student, checked_in=timezone.now())
        serializer = self.get_serializer(log)
        return Response({
            'message': 'Check-in successful',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)
class CheckOutView(generics.UpdateAPIView):
    queryset = LibraryLog.objects.all()
    serializer_class = LibraryLogSerializer

    def update(self, request, *args, **kwargs):
        student_id = request.data.get("student_id")

        # Lấy sinh viên từ Student
        try:
            student = Student.objects.get(student_id=student_id)
        except Student.DoesNotExist:
            raise ValidationError({"student_id": "Student with this ID does not exist."})
        
        # Tìm bản ghi check-in chưa có thời gian check-out
        log = LibraryLog.objects.filter(student=student, checked_out__isnull=True).first()

        # Cập nhật thời gian check-out
        log.checked_out = timezone.now()
        log.save()
        serializer = self.get_serializer(log)

        return Response({
            "message": "Check-out successful",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
#BookTranscaction
class BookTransactionAddView(generics.CreateAPIView):
    queryset = BookTransaction.objects.all()
    serializer_class = BookTransactionSerializer

    def create(self, request, *args, **kwargs):
        student_id = request.data.get('student_id')
        book_id = request.data.get('book_id')
        days_registered = request.data.get('day_registered')

        # Kiểm tra sự tồn tại của sinh viên và sách
        try:
            student = Student.objects.get(student_id=student_id)
        except Student.DoesNotExist:
            return Response({'message': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

        # Kiểm tra xem sách còn tồn kho
        if book.quantity <= 0:
            return Response({'message': 'Book not available'}, status=status.HTTP_400_BAD_REQUEST)

        # Tạo giao dịch mượn sách
        transaction = BookTransaction.objects.create(
            student=student,
            book=book,
            borrow_date=timezone.now(),
            days_registered = days_registered
        )
        serializers = self.get_serializer(transaction)
        # Giảm số lượng sách còn lại trong thư viện
        book.quantity -= 1
        book.save()

        return Response({
            'message': 'Book borrowed successfully!',
            'data': serializers.data
        }, status=status.HTTP_201_CREATED)
class BookTransactionSearchView(generics.ListAPIView):
    serializer_class = BookTransactionSerializer
    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)  # Sử dụng phương thức `list` của `ListAPIView`
    def get_queryset(self):
        queryset = BookTransaction.objects.all()

        student_id = self.request.data.get('student_id', None)
        book_id = self.request.data.get('book_id', None)
        day_remaining = self.request.data.get('day_remaining', None)

        if student_id:
            queryset = queryset.filter(student__student_id=student_id)
        if book_id:
            queryset = queryset.filter(book__id=book_id)
        
        if day_remaining is not None:
            today = timezone.now().date()
            # Tính toán số ngày còn lại và lọc theo điều kiện
            queryset = queryset.annotate(
            remainday=F('days_registered') - (today - F('borrow_date')).days
            ).filter(remainday__gte=int(day_remaining))
        return queryset
class UpdateTransactionStatusView(APIView):
    def post(self, request, *args, **kwargs):
        transac_id = request.data.get('transac_id')
        
        # Kiểm tra sự tồn tại của giao dịch
        try:
            transaction = BookTransaction.objects.get(id=transac_id)
        except BookTransaction.DoesNotExist:
            return Response({'error': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Cập nhật ngày trả nếu chưa có và hoàn tất giao dịch
        if not transaction.return_date:
            transaction.return_date = timezone.now()  # Đặt ngày trả thành ngày hiện tại
            transaction.save()
            
            # Tăng số lượng sách
            book = transaction.book
            book.quantity += 1
            book.save()

            return Response({
                'message': 'Transaction updated to returned status successfully!',
                'transaction_id': transac_id
            }, status=status.HTTP_200_OK)
        
        return Response({'error': 'Transaction is already marked as returned'}, status=status.HTTP_400_BAD_REQUEST)