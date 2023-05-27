from django.shortcuts import render
from .models import Faculty
import json
from django.http import JsonResponse

# Create your views here.

def home(request):    
    return render(request, "index.html")


def faculty(request):
    faculties = Faculty.objects.all()
    return render(request, "faculty.html", context={"faculties": faculties})

def option(request, faculty):
    query_data = {}

    
    cleaned_faculty_name = faculty.replace("-", " ")
    faculty_data = Faculty.objects.get(faculty_name=cleaned_faculty_name)
    
    for department in faculty_data.departments.all():
        query_data[department.department_name] = []
        for session in department.sessions.all():
            session_dict = {session.session_year: []}
            for level in session.levels.all():
                level_dict = {level.level: []}
                for semester in level.semesters.all():
                    semester_dict = {semester.semester_name: []}
                    for course in semester.courses.all():
                        semester_dict[semester.semester_name].append(course.name)
                    level_dict[level.level].append(semester_dict)
                session_dict[session.session_year].append(level_dict)
            query_data[department.department_name].append(session_dict)
    # if request.method == "POST":
    #     pass
    return render(request, "options.html", context={"json_query": json.dumps(query_data)})