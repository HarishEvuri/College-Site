from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teacher/<int:assign_id>/ClassDates/', views.t_class_date, name='t_class_date'),
    path('teacher/<int:assign_id>/AssignmentDates/', views.t_assignment_date, name='t_assignment_date'),
    path('teacher/<int:ass_c_id>/Edit_att/', views.edit_att, name='edit_att'),
    path('teacher/<int:ass_c_id>/Edit_ass/', views.edit_assignment, name='edit_assignment'),
    path('teacher/<int:ass_c_id>/attendance/confirm/', views.confirm, name='confirm'),
    path('teacher/<int:ass_c_id>/assignment/confirm/', views.assignment_confirm, name='assignment_confirm'),
    path('teacher/<int:assign_id>/Extra_class/', views.t_extra_class, name='t_extra_class'),
    path('teacher/<int:assign_id>/Extra_assignment/', views.t_extra_assignment, name='t_extra_assignment'),
    path('teacher/<slug:assign_id>/Extra_class/confirm/', views.e_confirm, name='e_confirm'),
    path('teacher/<slug:assign_id>/Extra_assignment/confirm/', views.e_assignment_confirm, name='e_assignment_confirm'),
    path('student/<slug:stud_id>/<slug:course_id>/attendance/', views.attendance_detail, name='attendance_detail'),
    path('student/<slug:stud_id>/<slug:course_id>/assignment/', views.assignment_detail, name='assignment_detail'),
]
