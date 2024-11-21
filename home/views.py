import datetime
from django.forms import DateTimeField, ValidationError
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
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Q, Count, F, ExpressionWrapper
from django.db.models.functions import TruncDay

class CustomPagination(PageNumberPagination):
    
    page_size = 10  # Số lượng mục mỗi trang mặc định
    page_size_query_param = 'page_size'  # Cho phép người dùng chỉ định page_size
    max_page_size = 100  # Số lượng tối đa mục mỗi trang
    def get_paginated_response(self, data):
        return Response({
            'message' : 'OK',
            'count': self.page.paginator.count,             # Tổng số phần tử
            'total_pages': self.page.paginator.num_pages,   # Tổng số trang
            'current_page': self.page.number,               # Trang hiện tại
            'results': data                                 # Dữ liệu của trang hiện tại
        })

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
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        # Lấy dữ liệu phân trang từ `self.list` và xử lý lại
        response = self.list(request, *args, **kwargs)
        paginated_data = response.data
        # Thêm các thông tin phân trang vào cấu trúc dữ liệu
        response.data = {
            "message" : paginated_data['message'],
            "total_elements": paginated_data['count'],  # Tổng số phần tử
            "total_pages": paginated_data['total_pages'],  # Tổng số trang
            "current_page": paginated_data['current_page'],  # Trang hiện tại
            "results": paginated_data['results'],  # Kết quả cho trang hiện tại
        }
        return response
    def get_queryset(self):
        title = self.request.data.get("title", "")
        author = self.request.data.get("author", "")
        category = self.request.data.get("category", "")
        order_by = self.request.data.get('order_by', "title")
        order = self.request.data.get('order', "")
        queryset = Book.objects.all()
        if not order_by:
            order_by = "title"  # Mặc định sắp xếp theo title nếu order_by không hợp lệ
        if not order:
            order = 'ASC'
        # Áp dụng các bộ lọc nếu có tham số tìm kiếm
        if title or author or category:
            filters = Q()
            if title:
                filters |= Q(title__icontains=title)  # Tìm theo tiêu đề
            if author:
                filters |= Q(author__icontains=author)  # Tìm theo tác giả
            if category:
                filters |= Q(category__icontains=category)  # Tìm theo thể loại
            queryset = queryset.filter(filters)
         # Sắp xếp theo trường `order_by`
        if order == 'ASC':
            queryset = queryset.order_by(order_by)  # Sắp xếp theo thứ tự tăng dần
        elif order == 'DESC':
            queryset = queryset.order_by(f"-{order_by}")  # Sắp xếp theo thứ tự giảm dần
    
        return queryset

class DeleteBookView(generics.DestroyAPIView):#checked
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]
    def delete(self, request, *args, **kwargs):
        book_id = self.request.query_params.get('id')
        if not book_id:
            return Response({
                'message':"'Book id is required."
            },status=status.HTTP_400_BAD_REQUEST)
        book = get_object_or_404(Book, id = book_id)
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
            # token = Token.objects.create(token=access_token)
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
class StudentDetailView(generics.RetrieveAPIView):#checked
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    def retrieve(self, request, *args, **kwargs):
        # Lấy student_id từ query parameter
        student_id = request.query_params.get('student_id')
        
        # Kiểm tra nếu student_id không tồn tại trong query parameters
        if not student_id:
            # Trả về phản hồi lỗi nếu không có student_id
            return Response({
                'message': 'student_id query parameter is required.'
            }, status=status.HTTP_400_BAD_REQUEST)

        # Sử dụng get_object_or_404 để tìm Student hoặc trả về 404 nếu không tìm thấy
        student = get_object_or_404(Student, student_id=student_id)
        serializer = self.get_serializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
class StudentAddView(generics.CreateAPIView):#checked
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
class StudentEditView(generics.UpdateAPIView):#checked
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
class StudentDeleteView(generics.DestroyAPIView):#checked
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated]
    def delete(self, request, *args, **kwargs):
        student_id = self.request.query_params.get('student_id')
        if not student_id:
            return Response({
                'message': 'student_id query parameter is required.'
            }, status=status.HTTP_400_BAD_REQUEST)
        student = get_object_or_404(Student, student_id = student_id)
        student.delete()
        return Response({'message': 'Delete Successfully'}, status= status.HTTP_204_NO_CONTENT)
class StudentSearchView(generics.ListAPIView):#checked
    serializer_class = StudentSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        # Lấy dữ liệu phân trang từ `self.list` và xử lý lại
        response = self.list(request, *args, **kwargs)
        paginated_data = response.data
        # Thêm các thông tin phân trang vào cấu trúc dữ liệu
        response.data = {
            'message': paginated_data["message"],
            "total_elements": paginated_data['count'],  # Tổng số phần tử
            "total_pages": paginated_data['total_pages'],  # Tổng số trang
            "current_page": paginated_data['current_page'],  # Trang hiện tại
            "results": paginated_data['results'],  # Kết quả cho trang hiện tại
        }
        return response
    def get_queryset(self):
        queryset = Student.objects.all()
        name = self.request.data.get("name", "")
        student_class = self.request.data.get("student_class","")  
        order_by = self.request.data.get("order_by", "")
        order = self.request.data.get("order", "")
        if not order_by:
            order_by = "name"
        if not order:
            order = 'ASC'
        if name or student_class:
            filters = Q()
            if name:
                filters |= Q(name__icontains=name)
            if student_class:
                filters |= Q(student_class__icontains=student_class)
            queryset = queryset.filter(filters)

        if order == 'ASC':
            queryset = queryset.order_by(order_by)  # Sắp xếp theo thứ tự tăng dần
        elif order == 'DESC':
            queryset = queryset.order_by(f"-{order_by}")  # Sắp xếp theo thứ tự giảm dần
        return queryset
#--------- LibraryLog-----
class CheckInView(generics.CreateAPIView):#checked
    serializer_class = LibraryLogSerializer
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        student_id = request.data.get('student_id')

        # Kiểm tra xem student_id có tồn tại trong request không
        if not student_id:
            raise serializers.ValidationError({"student_id": "Student ID is required."})
        existing_log = LibraryLog.objects.filter(student_id=student_id, checked_out__isnull=True).first()
        if existing_log:
            return Response({
                'message': 'Student has not checked out yet. Check-out is required before check-in.'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        log = LibraryLog.objects.create(student_id=student_id)

        # Lấy dữ liệu đã được serialize để trả về
        serializer = self.get_serializer(log)

        return Response({
            'message': 'Check-in successful',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)
class CheckOutView(generics.UpdateAPIView):#checked
    queryset = LibraryLog.objects.all()
    serializer_class = LibraryLogSerializer
    permission_classes = [IsAuthenticated]
    def update(self, request, *args, **kwargs):
        student_id = request.data.get("student_id")
     
        # Tìm bản ghi check-in chưa có thời gian check-out
        log = LibraryLog.objects.filter(student_id=student_id, checked_out__isnull=True).first()

        # Cập nhật thời gian check-out
        log.checked_out = int(time.time())
        log.save()
        serializer = self.get_serializer(log)

        return Response({
            "message": "Check-out successful",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
class GetStudentInLibraryView(generics.ListAPIView):
    serializer_class = LibraryLogSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        # Lấy dữ liệu phân trang từ `self.list` và xử lý lại
        response = self.list(request, *args, **kwargs)
        paginated_data = response.data
        # Thêm các thông tin phân trang vào cấu trúc dữ liệu
        response.data = {
            "message" : paginated_data['message'],
            "total_elements": paginated_data['count'],  # Tổng số phần tử
            "total_pages": paginated_data['total_pages'],  # Tổng số trang
            "current_page": paginated_data['current_page'],  # Trang hiện tại
            "results": paginated_data['results'],  # Kết quả cho trang hiện tại
        }
        return response
    def get_queryset(self):
        check = bool(self.request.data.get("check"))
        if not check:
            check = False
        if check == False:
            queryset = LibraryLog.objects.filter(checked_out__isnull=True)
        elif check == True:
            queryset = LibraryLog.objects.all()
        
        # Lọc theo mã sinh viên hoặc tên sinh viên nếu có
        student_id = self.request.data.get("student_id", "")
        name = self.request.data.get("name", "")
        order_by = self.request.data.get("order_by", "")
        order = self.request.data.get("order", "")
        if not order:
            order = 'ASC'
        if not order_by:
            order_by = 'student__name'
        queryset = queryset.select_related('student')
        filters = Q()
        if student_id:
            filters |= Q(student__student_id__icontains=student_id)  # Tìm theo mã sinh viên
        if name:
            filters |= Q(student__name__icontains=name)  # Tìm theo tên sinh viên
        queryset = queryset.filter(filters)
        if order == 'ASC':
            queryset = queryset.order_by(order_by)  # Sắp xếp theo thứ tự tăng dần
        elif order == 'DESC':
            queryset = queryset.order_by(f"-{order_by}")  # Sắp xếp theo thứ tự giảm 
        return queryset
#BookTranscaction
class BookTransactionAddView(generics.CreateAPIView):#checked
    queryset = BookTransaction.objects.all()
    serializer_class = BookTransactionSerializer
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        student_id = request.data.get('student_id')
        book_id = request.data.get('book_id')
        days_registered = request.data.get('days_registered')

        # Kiểm tra sự tồn tại của sinh viên và sách
        try:
            student = Student.objects.get(student_id=student_id)
        except Student.DoesNotExist:
            return Response({'message': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        #Sinh viên mượn sách phải trả cuốn sách đó mới được mượn lại
        if BookTransaction.objects.filter(student=student,book = book, return_date__isnull=True).exists():
            return Response({
                'message': 'Student has not returned the previous book. Please return the book first.'
            }, status=status.HTTP_400_BAD_REQUEST)
        # Kiểm tra xem sách còn tồn kho
        if book.quantity <= 0:
            return Response({'message': 'Book not available'}, status=status.HTTP_400_BAD_REQUEST)

        # Tạo giao dịch mượn sách
        transaction = BookTransaction.objects.create(
            student=student,
            book=book,
            borrow_date=int(time.time()),
            days_registered = days_registered
        )
        serializer = self.get_serializer(transaction)
        # Giảm số lượng sách còn lại trong thư viện
        book.quantity -= 1
        book.save()

        return Response({
            'message': 'Book borrowed successfully!',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)
class BookTransactionSearchView(generics.ListAPIView):#checked
    serializer_class = BookTransactionSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    def post(self, request, *args, **kwargs):
        # Lấy dữ liệu phân trang từ `self.list` và xử lý lại
        response = self.list(request, *args, **kwargs)
        paginated_data = response.data
        
        # Thêm các thông tin phân trang vào cấu trúc dữ liệu
        response.data = {
            'message': paginated_data["message"],
            "total_elements": paginated_data['count'],  # Tổng số phần tử
            "total_pages": paginated_data['total_pages'],  # Tổng số trang
            "current_page": paginated_data['current_page'],  # Trang hiện tại
            "results": paginated_data['results'],  # Kết quả cho trang hiện tại
        }
        
        return response
    def get_queryset(self):
        queryset = BookTransaction.objects.all()
        queryset = queryset.filter(return_date__isnull=True)
        student_id = self.request.data.get('student_id', None)
        book_id = self.request.data.get('book_id', None)
        day_remaining = self.request.data.get('day_remaining', "")
        order_by = self.request.data.get('order_by', "")
        if not order_by:
            order_by = "student_id"
        order = self.request.data.get('order', "")
        filters = Q()  
        if student_id:
            filters |= Q(student__student_id=student_id)  
        if book_id:
            filters |= Q(book__id=book_id)
        queryset = queryset.filter(filters)
        if day_remaining:
            today = timezone.now().date()
            filtered_queryset = []
            for i in queryset:
                borrow_date = datetime.date.fromtimestamp(i.borrow_date)
                return_date = borrow_date + datetime.timedelta(days=i.days_registered)
                remain_day = (return_date - today).days
                if remain_day >= int(day_remaining):
                  filtered_queryset.append(i)  # Thêm đối tượng vào danh sách nếu thỏa mãn điều kiện
            queryset = filtered_queryset

        
        if order == 'ASC':
            queryset = sorted(queryset, key=lambda x: getattr(x, order_by))
        elif order == 'DESC':
            queryset = sorted(queryset, key=lambda x: getattr(x, order_by), reverse=True)
        return queryset

class GetExpriedBookView(generics.ListAPIView):#checked
    serializer_class = BookTransactionSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    def post(self, request, *args, **kwargs):
        # Lấy dữ liệu phân trang từ `self.list` và xử lý lại
        response = self.list(request, *args, **kwargs)
        paginated_data = response.data
  
        # Thêm các thông tin phân trang vào cấu trúc dữ liệu
        response.data = {
            'message': paginated_data["message"],
            "total_elements": paginated_data['count'],  # Tổng số phần tử
            "total_pages": paginated_data['total_pages'],  # Tổng số trang
            "current_page": paginated_data['current_page'],  # Trang hiện tại
            "results": paginated_data['results'],  # Kết quả cho trang hiện tại
        }
        
        return response
    def get_queryset(self):
        queryset = BookTransaction.objects.all()
        queryset = queryset.filter(return_date__isnull=True)
        student_id = self.request.data.get('student_id', None)
        book_id = self.request.data.get('book_id', None)
        order_by = self.request.data.get('order_by', "")
        if not order_by:
            order_by = "student_id"
        order = self.request.data.get('order', "")
        if not order:
            order = 'ASC'
        filters = Q()  
        if student_id:
            filters |= Q(student__student_id=student_id)  
        if book_id:
            filters |= Q(book__id=book_id)
        queryset = queryset.filter(filters)
        
        today = timezone.now().date()
        filtered_queryset = []
        for i in queryset:
            borrow_date = datetime.date.fromtimestamp(i.borrow_date)
            return_date = borrow_date + datetime.timedelta(days=i.days_registered)
            if return_date < today:
                filtered_queryset.append(i)  # Thêm đối tượng vào danh sách nếu thỏa mãn điều kiện
        queryset = filtered_queryset
        if order == 'ASC':
            queryset = sorted(queryset, key=lambda x: getattr(x, order_by))
        elif order == 'DESC':
            queryset = sorted(queryset, key=lambda x: getattr(x, order_by), reverse=True)
        return queryset
class ExpiredBooksCountView(generics.ListAPIView):
    queryset = BookTransaction.objects.all()
    def list(self, request, *args, **kwargs):
        # Lấy danh sách các giao dịch quá hạn
        today = timezone.now().date()
        queryset = BookTransaction.objects.filter(
            return_date__isnull=True,  # Chưa trả sách
        )
        expired_count = 0

        for i in queryset:
            borrow_date = datetime.date.fromtimestamp(i.borrow_date)
            return_date = borrow_date + datetime.timedelta(days=i.days_registered)
            if return_date < today:
                expired_count += 1
        
        # Trả về số lượng giao dịch quá hạn
        return Response({"expired_books_count": expired_count})

class BookTransactionReturnView(generics.UpdateAPIView):#checked
    queryset = BookTransaction.objects.all()
    serializer_class = BookTransactionSerializer
    permission_classes = [IsAuthenticated]
    def update(self, request, *args, **kwargs):
        # Lấy mã sinh viên và mã sách từ body request
        student_id = request.data.get('student_id')
        book_id = request.data.get('book_id')

        if not student_id or not book_id:
            return Response({'error': 'Both student_id and book_id are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Tìm giao dịch theo student_id và book_id
        try:
            transaction = BookTransaction.objects.get(student__student_id=student_id, book__id=book_id, return_date__isnull=True)
        except BookTransaction.DoesNotExist:
            return Response({'error': 'Transaction not found or the book has already been returned.'}, status=status.HTTP_404_NOT_FOUND)

        # Cập nhật ngày trả nếu chưa có và hoàn tất giao dịch
        if not transaction.return_date:
            transaction.return_date = int(time.time()) # Đặt ngày trả thành ngày hiện tại
            transaction.save()
            # Tăng số lượng sách
            book = transaction.book
            book.quantity += 1
            book.save()
            serializer = self.get_serializer(transaction)
            return Response({
                'message': 'Book successfully returned!',
                'data': serializer.data
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Transaction is already marked as returned'}, status=status.HTTP_400_BAD_REQUEST)
class LibraryLogCountInDayView(APIView):
    def post(self, request):
        # Lấy tham số 'count' từ body
        count = request.data.get('count')

        # Kiểm tra nếu count không hợp lệ
        if not count or not isinstance(count, int) or count <= 0:
            return Response({'error': 'Tham số count không hợp lệ.'}, status=status.HTTP_400_BAD_REQUEST)

        # Lấy ngày hiện tại
        today = timezone.now().date()

        # Tính toán ngày bắt đầu (count ngày trước từ hôm nay, bao gồm cả hôm nay)
        start_date = today - datetime.timedelta(days=count - 1)  # Bao gồm ngày hôm nay

        # Danh sách tất cả các ngày từ start_date đến hôm nay
        all_days = [start_date + datetime.timedelta(days=i) for i in range(count)]

        # Chuẩn bị dữ liệu trả về
        response_data = []

        # Kiểm tra các ngày và thêm dữ liệu vào response
        for day in all_days:
            # Chuyển đổi ngày thành Unix timestamp
            day_start = int(time.mktime(day.timetuple()))
            day_end = int(time.mktime((day + datetime.timedelta(days=1)).timetuple()))  # Tính đến cuối ngày
            
            # Truy vấn và đếm số lượt check-in trong ngày
            day_logs = LibraryLog.objects.filter(
                checked_in__gte=day_start,
                checked_in__lt=day_end
            ).count()  # Đếm số lượt check-in trong ngày

            # Thêm vào dữ liệu trả về
            response_data.append({
                'timestamp': day_start,  # Chuyển đổi ngày thành Unix timestamp
                'check_in_count': day_logs,  # Số lượt check-in trong ngày
                'date': day.strftime('%Y-%m-%d')  # Định dạng lại ngày theo 'YYYY-MM-DD'
            })

        return Response(response_data, status=status.HTTP_200_OK)
class CategoryAddView(generics.CreateAPIView):#checked
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        serializers =CategorySerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({
                'message': 'Category added sucessfully!',
                'data': serializers.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": 'Failed to add Category',
            'errors' : serializers.errors
        }, status= status.HTTP_400_BAD_REQUEST)
    
class CategoryEditview(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):#checked
        category_id = self.request.data.get("category_id")
        if not category_id:
            raise ValidationError({"message": "Category_id is requierd"})
        return get_object_or_404(Category,id = category_id)
    def update(self, request, *args, **kwargs):
        category = self.get_object()
        serializers = CategorySerializer(category, data = request.data, partial = True)
        if serializers.is_valid():
            serializers.save()
            return Response({
                'message':"category update Success",
                'data' : serializers.data
            }, status= status.HTTP_200_OK)
        return Response({
            'errors': "Failed to update category_id",
            'data': serializers.errors
        },status= status.HTTP_400_BAD_REQUEST)
class CatergoryDeleteView(generics.DestroyAPIView):#checked
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]
    def delete(self, request, *args, **kwargs):
        category_id = self.request.query_params.get('category_id')
        if not category_id:
            return Response({
                'message': 'category_id query parameter is required.'
            }, status=status.HTTP_400_BAD_REQUEST)
        student = get_object_or_404(Category, id = category_id)
        student.delete()
        return Response({'message': 'Delete Successfully'}, status= status.HTTP_204_NO_CONTENT)
class CategoryAllView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer