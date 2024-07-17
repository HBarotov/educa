from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("courses", views.CourseViewSet)
router.register("subjects", views.SubjectViewSet)

app_name = "courses"
urlpatterns = [
    path("", include(router.urls)),
]
