from django.shortcuts import redirect
from django.http import Http404
from student.models import Student
from student.forms import AddStudentForm,AddStudentModelForm
from django.views import View

def delete_student(request, id):
    record = Student.objects.get(id=id)
    if record:
        record.delete()
        if request.session.get('selected_students'):
            request.session.pop('selected_students')
        #     for record in request.session['selected_students']:
        #         print(record['id'],type(record['id']))
        #         print(id, type(id))
        #         if str(record['id']) == id:
        #             request.session['selected_students'].pop(record)
        #             # print(request.session['selected_students'])
        return redirect('home')
    else:
        raise Http404('No student was found matching to the given id!')


def create_student(request):
    if request.method == 'POST':
        # form = AddStudentForm(request.POST)
        form = AddStudentModelForm(request.POST)
        if form.is_valid():
            # Student.objects.create(name=request.POST['name'])
            form.save()
            if request.session.get('selected_students'):
                request.session.pop('selected_students')
            return redirect('home')
        else:
            raise Http404("Error Occurred")


class UpdateStudent(View):
    def get(self, request):
        pass

    def post(self, request, id):
        # form = AddStudentForm(request.POST)
        form = AddStudentModelForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            record = Student.objects.get(id=id)
            record.name = name
            record.save()
            if request.session.get('selected_students'):
                request.session.pop('selected_students')
            return redirect('home')
        else:
            raise Http404("Problem with form")


def update_student(request, id):
    if request.method == 'POST':
        name = request.POST.get('student_name')
        record = Student.objects.get(id=id)
        if record:
            print(record.name, "1st")
            record.name = name
            print(record.name, "2nd")
            record.save()
            if request.session.get('selected_students'):
                request.session.pop('selected_students')
            return redirect('home')
        else:
            raise Http404('No student was found matching to the given id!')


def select_student(request):
    if request.method == 'GET':
        name = request.GET.get('student_name')
        records = Student.objects.filter(name=name)
        if records:
            request.session['selected_students'] = list(records.values())
            return redirect('home')
        else:
            raise Http404('No student was found matching to the given id!')
