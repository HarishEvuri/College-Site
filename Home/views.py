from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Dept, Class, Student, Attendance, Course, Teacher, Assign, AttendanceTotal, AttendanceClass, AssignmentClass, Assignment
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    if request.user.is_teacher:
        teacher = request.user.teacher
        ass_list = Assign.objects.filter(teacher=teacher)
        return render(request, 'Home/t_homepage.html', {'ass_list': ass_list})
    if request.user.is_student:
        stud = request.user.student
        ass_list = Assign.objects.filter(class_id=stud.class_id).order_by('class_id')
        return render(request, 'Home/homepage.html', {'ass_list': ass_list})
    return render(request, 'Home/logout.html')


@login_required()
def t_class_date(request, assign_id):
    now = timezone.now()
    ass = get_object_or_404(Assign, id=assign_id)
    att_list = ass.attendanceclass_set.order_by('-date')
    return render(request, 'Home/t_class_date.html', {'att_list': att_list, 'ass': ass})

@login_required()
def t_assignment_date(request, assign_id):
    ass = get_object_or_404(Assign, id=assign_id)
    assignment_list = ass.assignmentclass_set.order_by('-date')
    return render(request, 'Home/t_assignment_date.html', {'ass_list': assignment_list, 'ass': ass})


@login_required()
def edit_att(request, ass_c_id):
    assc = get_object_or_404(AttendanceClass, id=ass_c_id)
    cr = assc.assign.course
    att_list = Attendance.objects.filter(attendanceclass=assc, course=cr)
    context = {
        'assc': assc,
        'att_list': att_list,
    }
    return render(request, 'Home/t_edit_att.html', context)

@login_required()
def edit_assignment(request, ass_c_id):
    assc = get_object_or_404(AssignmentClass, id=ass_c_id)
    cr = assc.assign.course
    ass_list = Assignment.objects.filter(assignmentclass=assc, course=cr)
    context = {
        'assc': assc,
        'ass_list': ass_list,
    }
    return render(request, 'Home/t_edit_assignment.html', context)

@login_required()
def confirm(request, ass_c_id):
    assc = get_object_or_404(AttendanceClass, id=ass_c_id)
    ass = assc.assign
    cr = ass.course
    cl = ass.class_id
    count = 0
    for i, s in enumerate(cl.student_set.all()):
        status = request.POST[s.roll_number]
        if status == 'present':
            status = 'True'
            count = count + 1
        else:
            status = 'False'
        try:
            a = Attendance.objects.get(course=cr, student=s, date=assc.date, attendanceclass=assc)
            a.status = status
            a.save()
        except Attendance.DoesNotExist:
            a = Attendance(course=cr, student=s, status=status, date=assc.date, attendanceclass=assc)
            a.save()
    assc.status = count
    assc.save()

    return HttpResponseRedirect(reverse('t_class_date', args=(ass.id,)))

@login_required()
def assignment_confirm(request, ass_c_id):
    assc = get_object_or_404(AssignmentClass, id=ass_c_id)
    ass = assc.assign
    cr = ass.course
    cl = ass.class_id
    for i, s in enumerate(cl.student_set.all()):
        marks = request.POST[s.roll_number]
        if assc.status == 1:
            try:
                a = Assignment.objects.get(course=cr, student=s, date=assc.date, assignmentclass=assc)
                a.marks = marks
                a.save()
            except Attendance.DoesNotExist:
                a = Attendance(course=cr, student=s, marks=marks, date=assc.date, assignmentclass=assc)
                a.save()
        else:
            a = Attendance(course=cr, student=s, marks=marks, date=assc.date, assignmentclass=assc)
            a.save()
            assc.status = 1
            assc.save()

    return HttpResponseRedirect(reverse('t_assignment_date', args=(ass.id,)))


@login_required()
def t_extra_class(request, assign_id):
    ass = get_object_or_404(Assign, id=assign_id)
    c = ass.class_id
    context = {
        'ass': ass,
        'c': c,
    }
    return render(request, 'Home/t_extra_class.html', context)

@login_required()
def t_extra_assignment(request, assign_id):
    ass = get_object_or_404(Assign, id=assign_id)
    c = ass.class_id
    context = {
        'ass': ass,
        'c': c,
    }
    return render(request, 'Home/t_extra_assignment.html', context)


@login_required()
def e_confirm(request, assign_id):
    ass = get_object_or_404(Assign, id=assign_id)
    cr = ass.course
    cl = ass.class_id
    assc = ass.attendanceclass_set.create(status=0, date=request.POST['date'])
    count = 0
    assc.save()

    for i, s in enumerate(cl.student_set.all()):
        status = request.POST[s.roll_number]
        if status == 'present':
            status = 'True'
            count = count+1
        else:
            status = 'False'
        date = request.POST['date']
        a = Attendance(course=cr, student=s, status=status, date=date, attendanceclass=assc)
        a.save()
    
    assc.status = count
    assc.save()
    return HttpResponseRedirect(reverse('t_class_date', args=(ass.id,)))


@login_required()
def e_assignment_confirm(request, assign_id):
    ass = get_object_or_404(Assign, id=assign_id)
    cr = ass.course
    cl = ass.class_id
    assc = ass.assignmentclass_set.create(status=1, date=request.POST['date'], name=request.POST['name'], maxmarks=request.POST['maxmarks'])
    assc.save()

    for i, s in enumerate(cl.student_set.all()):
        marks = request.POST[s.roll_number]
        date = request.POST['date']
        a = Assignment(course=cr, student=s, marks=marks, date=date, assignmentclass=assc)
        a.save()

    return HttpResponseRedirect(reverse('t_assignment_date', args=(ass.id,)))

@login_required()
def attendance_detail(request, stud_id, course_id):
    stud = get_object_or_404(Student, roll_number=stud_id)
    cr = get_object_or_404(Course, id=course_id)
    att_list = Attendance.objects.filter(course=cr, student=stud).order_by('-date')
    count = Attendance.objects.filter(course=cr, student=stud, status='True').count()
    return render(request, 'Home/att_detail.html', {'att_list': att_list, 'cr': cr, 'count': count})

@login_required()
def assignment_detail(request, stud_id, course_id):
    stud = get_object_or_404(Student, roll_number=stud_id)
    cr = get_object_or_404(Course, id=course_id)
    ass_list = Assignment.objects.filter(course=cr, student=stud).order_by('-date')
    return render(request, 'Home/ass_detail.html', {'ass_list': ass_list, 'cr': cr})