from django.shortcuts import render
from student.models import Student
from django.http import Http404


def delete_student(request, id):
    record = Student.objects.get(id=id)
    if record:
        record.delete()
        students = Student.objects.all()
        context = {'students': students}
        return render(request, 'user/home.html', context)
    else:
        return Http404('No student was found matching to the given id!')


def create_student(request):
    if request.method == 'POST':
        name = request.POST.get('student_name')
        Student.objects.create(name=name)
    students = Student.objects.all()
    context = {'students':students}
    return render(request, 'user/home.html',context)


def update_student(request, id):
    if request.method == 'POST':
        name = request.POST.get('student_name')
        record = Student.objects.get(id=id)
        if record:
            print(record.name, "1st")
            record.name = name
            print(record.name, "2nd")
            record.save()
            students = Student.objects.all()
            context = {'students': students}
            return render(request, 'user/home.html', context)
        else:
            return Http404('No student was found matching to the given id!')


def select_student(request):
    if request.method == 'GET':
        name = request.GET.get('student_name')
        records = Student.objects.all().filter(name=name)
        if records:
            students = Student.objects.all()
            context = {'selected_students': records,'students':students}
            return render(request, 'user/home.html', context)
        else:
            return Http404('No student was found matching to the given id!')
