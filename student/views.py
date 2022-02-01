from django.shortcuts import render,redirect
from student.models import Student
from django.http import Http404,HttpResponseRedirect


def delete_student(request, id):
    record = Student.objects.get(id=id)
    if record:
        record.delete()
        return redirect('home')
    else:
        return Http404('No student was found matching to the given id!')


def create_student(request):
    if request.method == 'POST':
        name = request.POST.get('student_name')
        Student.objects.create(name=name)

    return redirect('home')


def update_student(request, id):
    if request.method == 'POST':
        name = request.POST.get('student_name')
        record = Student.objects.get(id=id)
        if record:
            print(record.name, "1st")
            record.name = name
            print(record.name, "2nd")
            record.save()
            return redirect('home')
        else:
            return Http404('No student was found matching to the given id!')


def select_student(request):
    if request.method == 'GET':
        name = request.GET.get('student_name')
        records = Student.objects.all().filter(name=name)
        if records:
            students = Student.objects.all()
            context = {'selected_students': records, 'students': students}
            return render(request, 'user/home.html', context)
        else:
            return Http404('No student was found matching to the given id!')
