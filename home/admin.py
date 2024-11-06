from django.contrib import admin
from .models import Manager, Student, LibraryLog, Book, BookTransaction
# Register your models here.
class ManagerAdmin(admin.ModelAdmin):
    list_display = ["username", "password", "last_login"]
    search_fields = ["username"]
    list_filter = ["username"]
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Student)
admin.site.register(LibraryLog)
admin.site.register(Book)
admin.site.register(BookTransaction)