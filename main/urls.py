
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher/create_course/', views.create_course, name='create_course'),
    path('teacher/add_quiz/', views.add_quiz, name='add_quiz'),
    path('teacher/course/<int:course_id>/quizzes/', views.view_quizzes, name='view_quizzes'),
    path('teacher/quiz/<int:quiz_id>/add_questions/', views.add_questions, name='add_questions'),
    path('student/course/<int:course_id>/start_quiz/', views.start_quiz, name='start_quiz'),
    path('quiz/result/<int:quiz_id>/', views.quiz_result, name='quiz_result'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),
    path('sam/', views.samples, name='sam'),
]
