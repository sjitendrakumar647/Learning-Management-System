# main/admin.py

from django.contrib import admin
from .models import Profile, Course, Quiz, Question, StudentAnswer, Enrollment

admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(StudentAnswer)
admin.site.register(Enrollment)
