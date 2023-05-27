from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name="home"),
    path('faculty', views.faculty, name='faculties'),
    path("faculty/<slug:faculty>", views.option, name="faculty")
]