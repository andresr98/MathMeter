from django.db import models
from datetime import date

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    id_number = models.CharField(max_length=20)
    birth_date = models.DateField(null = True, blank = True)
    school = models.ForeignKey('School', on_delete = models.CASCADE)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    teacher = models.ForeignKey('Teacher', on_delete = models.SET_NULL, null = True, blank = True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete = models.CASCADE)

    def __str__(self):
        return self.category.name + ' -- ' + self.name

class Aspect(models.Model):
    objective = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    sub_cat = models.ForeignKey('SubCategory', on_delete = models.CASCADE)

    def __str__(self):
        return self.objective  + ' -- ' + self.sub_cat.category.name + ' -- ' + self.sub_cat.name

class Problem(models.Model):
    question = models.TextField()
    answer = models.FloatField()
    aspect = models.ForeignKey('Aspect', on_delete = models.CASCADE)

    def __str__(self):
        return self.question + ' -- ' + self.aspect.sub_cat.category.name + ' -- ' self.aspect.sub_cate.name + ' -- ' +self.aspect.name

class Group(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey('Teacher', on_delete = models.SET_NULL, null = True, blank = True)
    school = models.ForeignKey('School', on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
     name = models.CharField(max_length=200)

     def __str__(self):
        return self.name

class StudentXGroup(models.Model):
     id_school = models.CharField(max_length=200)
     group = models.ForeignKey('Group', on_delete = models.CASCADE)
     student = models.ForeignKey('Student', on_delete = models.CASCADE)

     def __str__(self):
        return self.group.name + ' -- ' + self.student.name

class Exam(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    teacher = models.ForeignKey('Teacher', on_delete = models.CASCADE)
    #Duration in minutes
    duration = models.IntegerField(default = 60)

    def __str__(self):
        return self.name

class Test(models.Model):
    exam = models.ForeignKey('Exam', on_delete = models.CASCADE)
    aspect = models.ForeignKey('Aspect', on_delete = models.CASCADE)
    weight = models.FloatField()

    def __str__(self):
        return self.exam.name + " -- " +  self.aspect.name + " -- " + str(self.weight)

class StudentAnswer(models.Model):
    test = models.ForeignKey('Test', on_delete = models.CASCADE)
    sxg = models.ForeignKey('StudentXGroup', on_delete = models.CASCADE)
    failed = models.BooleanField(default = True)
    date = models.DateField(null = True, blank = True, default = date.today)

    def __str__(self):
        if self.failed == True:
            return self.sxg.student.name + " -- " + self.test + " Fallo"
        return self.sxg.student.name + " -- " + self.test + " Acierto"