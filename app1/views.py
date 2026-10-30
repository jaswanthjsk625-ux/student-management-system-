
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'detail.html', {'student': student})

def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST.get('name'),
            roll_no=request.POST.get('roll'),
            course=request.POST.get('course'),
            fees=request.POST.get('fees')
        )
        return redirect('home')
    return render(request, 'add.html')

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.roll_no = request.POST.get('roll')
        student.course = request.POST.get('course')
        student.fees = request.POST.get('fees')
        student.save()
        return redirect('home')
    return render(request, 'edit.html', {'student': student})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('home')