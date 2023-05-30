from django import forms
from .models import Faculty



class RequestForm(forms.Form):
    faculty = forms.ChoiceField(choices=())
    department = forms.ChoiceField(choices=())
    session = forms.ChoiceField(choices=())
    semester = forms.ChoiceField(choices=())
    course = forms.ChoiceField(choices=())

    # def get_all_faculty():
    #     faculties = 
    #     query = Faculty.objects.all()



    