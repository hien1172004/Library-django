from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


# /managers/-GET
# /managers/-POST
#/managers/{id} -GET
#/managers/{id} -PUT
#/managers/{id} -DELETE
urlpatterns = [
    
    path('book/edit/<int:pk>/', BookUpdateAPIView.as_view(), name='book-edit'),  # Sửa sách
    path('book/delete/<int:pk>/', BookDeleteAPIView.as_view(), name='book-delete'),  # Xoá sách
    path('book/search/', BookSearchAPIView.as_view(), name='book-search'),  # Tìm kiếm sách
    path('book/add/', BookAddAPIView.as_view(), name = "book-add"), # Thêm sách
    path('user/login', LoginAPIView.as_view(), name='login'),
]
