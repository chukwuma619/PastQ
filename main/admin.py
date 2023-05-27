from django.contrib import admin
from .models import Faculty, Department, Session, Semester, Course, Level

# Register your models here.

admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Session)
admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(Level)