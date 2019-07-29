from django.contrib import admin

from .models import Category, SubCategory, Aspect, Problem, School, Teacher, Group, Student, StudentXGroup, Exam, Test, StudentAnswer
### mathmeter

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Aspect)
admin.site.register(Problem)
admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(StudentXGroup)
admin.site.register(Exam)
admin.site.register(Test)
admin.site.register(StudentAnswer)
