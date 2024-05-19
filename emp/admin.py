from django.contrib import admin
from .models import Employee


# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display=('name', 'working', 'emp_id', 'phone', 'department')
    list_editable=('working', 'emp_id')
    search_fields=('name', 'department')
    list_filter=('working', 'department')

admin.site.register(Employee, EmpAdmin)

