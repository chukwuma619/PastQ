from django.shortcuts import render
from .models import Faculty, Course
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
        
    if request.method == "GET":
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
        return render(request, "options.html", context={"json_query": json.dumps(query_data)})
    
    elif request.method == "POST":
        data = request.POST
        
        department = data["department"]
        session = data["session"]
        level = data["level"]
        semester = data["semester"]
        course_name = data["course"]

        department_instance = faculty_data.departments.filter(department_name=department)
        session_instance = department_instance[0].sessions.filter(session_year=session)
        year_instance = session_instance[0].levels.filter(level=level)
        semester_instance = year_instance[0].semesters.filter(semester_name=semester)
        course_instance = semester_instance[0].courses.filter(name=course_name)

        return render(request, "download.html", context={"file_url": course_instance[0].file})
        
   
    