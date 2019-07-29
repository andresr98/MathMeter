from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete = models.CASCADE)
    def __str__(self):
        return self.name

class Aspect(models.Model):
    objective = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    sub_cat = models.ForeignKey('SubCategory', on_delete = models.CASCADE)
    def __str__(self):
        return self.objective

class Problem(models.Model):
    question = models.TextField()
    answer = models.FloatField()
    aspect = models.ForeignKey('Aspect', on_delete = models.CASCADE)
    def __str__(self):
        return self.question

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
        return self.id_school

class Exam(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    teacher = models.ForeignKey('Teacher', on_delete = models.CASCADE)
    def __str__(self):
        return self.name

class Test(models.Model):
    exam = models.ForeignKey('Exam', on_delete = models.CASCADE)
    aspect = models.ForeignKey('Aspect', on_delete = models.CASCADE)
    weight = models.FloatField()
    def __str__(self):
        return str(self.weight)

class StudentAnswer(models.Model):
    test = models.ForeignKey('Test', on_delete = models.CASCADE)
    sxg = models.ForeignKey('StudentXGroup', on_delete = models.CASCADE)
    failed = models.BooleanField(default = True)
    def __str__(self):
        return str(self.test) +" "+ str(self.sxg)