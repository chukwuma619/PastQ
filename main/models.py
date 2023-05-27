from django.db import models

# Create your models here.

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=250, unique=True)

    def __str__(self) -> str:
        return self.faculty_name
    
class Department(models.Model):
    department_name = models.CharField(max_length=250, unique=True)
    faculty = models.ForeignKey(to=Faculty, on_delete=models.CASCADE, related_name="departments")
    
    def __str__(self) -> str:
        return self.department_name
    
class Session(models.Model):
    session_year = models.CharField(max_length=250, unique=True)
    department = models.ManyToManyField(to=Department, related_name="sessions")
    
    def __str__(self) -> str:
        return self.session_year

class Level(models.Model):
    level = models.CharField(max_length=250, unique=True)
    sessions = models.ManyToManyField(to=Session, related_name="levels")
    
    def __str__(self) -> str:
        return self.level
    
class Semester(models.Model):
    semester_name = models.CharField(max_length=250, unique=True)
    levels = models.ManyToManyField(to=Level, related_name="semesters")
    
    def __str__(self) -> str:
        return self.semester_name
    
class Course(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to="uploads/", unique=True)
    semester = models.ForeignKey(to=Semester, on_delete=models.CASCADE, related_name="courses")
    level = models.ForeignKey(to=Level, on_delete=models.CASCADE)
    session = models.ForeignKey(to=Session, on_delete=models.CASCADE)
    department = models.ManyToManyField(to=Department)

    def __str__(self) -> str:
        return self.name