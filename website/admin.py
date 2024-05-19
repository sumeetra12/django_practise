from django.contrib import admin
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=('name', 'college', 'age', 'is_active')

admin.site.register(Student, StudentAdmin)
