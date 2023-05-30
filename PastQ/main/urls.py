from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('faculty', views.faculty, name='faculties'),
    path("faculty/<slug:faculty>", views.option, name="faculty")
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)