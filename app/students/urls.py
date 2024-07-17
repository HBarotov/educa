from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path(
        "register/",
        views.StudentRegistrationView.as_view(),
        name="student_registration",
    ),
    path(
        "enroll-course/",
        views.StudentEnrollCourseView.as_view(),
        name="student_enroll_course",
    ),
    path(
        "courses/<int:pk>/<slug:slug>/",
        cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
        name="student_course_detail",
    ),
    path(
        "courses/<int:pk>/<slug:slug>/<int:module_id>/",
        cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
        name="student_course_detail_module",
    ),
    path("courses/", views.StudentCourseListView.as_view(), name="student_course_list"),
]
