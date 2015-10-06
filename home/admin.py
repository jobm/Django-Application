from django.contrib import admin
from home.models import Student,ClassRoom
from .forms import StudentForm
#define student admin
class StudentAdmin(admin.ModelAdmin):
    form = StudentForm
# Register your models here.
admin.site.register(Student,StudentAdmin)
admin.site.register(ClassRoom)
