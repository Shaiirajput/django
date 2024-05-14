from django.contrib import admin
from .models import Student,Resume

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']
       
    list_per_page=4
    list_editable=['name']
    search_fields=['name__startswith']
    list_filter=["name"]


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display=['id','name','email','dob','state','gender','location','pimage','rdoc']


