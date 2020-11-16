from django.contrib import admin
from .models import Dept, Class, Student, Course, Teacher, Assign, User, AttendanceClass, Attendance, AssignmentClass, Assignment
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class ClassInline(admin.TabularInline):
    model = Class
    extra = 0


class DeptAdmin(admin.ModelAdmin):
    inlines = [ClassInline]
    list_display = ('name', 'id')
    search_fields = ('name', 'id')
    ordering = ['name']


class StudentInline(admin.TabularInline):
    model = Student
    extra = 0


class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'dept', 'sem')
    search_fields = ('id', 'dept__name', 'sem')
    ordering = ['dept__name', 'sem']
    inlines = [StudentInline]


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'dept')
    search_fields = ('id', 'name', 'dept__name')
    ordering = ['dept', 'id']


class AttendanceClassInline(admin.TabularInline):
    model = AttendanceClass
    extra = 0

class AssignmentClassInline(admin.TabularInline):
    model = AssignmentClass
    extra = 0

class AssignAdmin(admin.ModelAdmin):
    list_display = ('class_id', 'course', 'teacher')
    search_fields = ('class_id', 'class_id__id',
                     'course__name', 'teacher__name', 'course__shortname')
    ordering = ['class_id__dept__name', 'class_id__id', 'course__id']
    inlines = [AttendanceClassInline, AssignmentClassInline]


class AttendanceInline(admin.TabularInline):
    model = Attendance
    extra = 0

class AssignmentInline(admin.TabularInline):
    model = Assignment
    extra = 0


class AttendanceClassAdmin(admin.ModelAdmin):
    list_display = ('assign', 'date', 'status')
    inlines = [AttendanceInline]

class AssignmentClassAdmin(admin.ModelAdmin):
    list_display = ('assign', 'name', 'date')
    inlines = [AssignmentInline]

class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'name', 'class_id')
    search_fields = ('roll_number', 'name', 'class_id__id',
                     'class_id__dept__name')
    ordering = ['class_id__dept__name', 'class_id__id', 'roll_number']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'dept')
    search_fields = ('name', 'dept__name')
    ordering = ['dept__name', 'name']


admin.site.register(User, UserAdmin)
admin.site.register(Dept, DeptAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Assign, AssignAdmin)
admin.site.register(AttendanceClass, AttendanceClassAdmin)
admin.site.register(AssignmentClass, AssignmentClassAdmin)