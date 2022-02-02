from django import forms
from student.models import Student


class AddStudentForm(forms.Form):
    name = forms.CharField(label="Student Name", max_length=40,widget=forms.TextInput(attrs={'class': 'form-control'}))


class AddStudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        labels = {
            "name": "Student Name Model Form"
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
