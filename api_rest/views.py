from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
import random

# Create your views here.
def index(request):
    return HttpResponse("Hello, You are in API_REST of MathMeter")

#Vistas siempre en plurales
class Groups(APIView):
    def post(self, req):
        try:
            body = req.data
            id_teacher = body['id_teacher']

            grupos = Group.objects.values('id', 'name', 'school__name').filter(teacher_id=id_teacher)
            return Response({"status": status.HTTP_200_OK, "entity": grupos, "error":""}, status = status.HTTP_200_OK)

        except KeyError:
             return Response({"status": status.HTTP_400_BAD_REQUEST, "entity": "", "error":"Campos ingresados de forma incorrecta"},\
             status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"status": status.HTTP_404_NOT_FOUND, "entity":"", "error":"No hay datos en la base de datos"},\
             status= status.HTTP_404_NOT_FOUND)

class Categories(APIView):
    def get(self, req, id):
        try:
            category = Category.objects.values('id','name').get(id=id)
            subcat = SubCategory.objects.values('id', 'name').filter(category_id=id)
            return Response({"status": status.HTTP_200_OK, "entity": {'category': category,'subcat': subcat} ,"error":""}, status = status.HTTP_200_OK)
        except KeyError:
             return Response({"status": status.HTTP_400_BAD_REQUEST, "entity": "", "error":"Campos ingresados de forma incorrecta"},\
             status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"status": status.HTTP_404_NOT_FOUND, "entity":"", "error":"No hay datos en la base de datos"},\
             status= status.HTTP_404_NOT_FOUND)

    def post(self, req):
        try:
            body = req.data
            id_teacher = body['id_teacher']
            option = body['option']

            if option == 0:
                #Crear una categoria
                print("Algo sucederá")
            elif option == 1:
                #Listar categorias
                categories = Category.objects.values('id','name').filter(teacher_id=id_teacher)
                return Response({"status": status.HTTP_200_OK, "entity": categories, "error":""}, status = status.HTTP_200_OK)
        except KeyError:
             return Response({"status": status.HTTP_400_BAD_REQUEST, "entity": "", "error":"Campos ingresados de forma incorrecta"},\
             status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"status": status.HTTP_404_NOT_FOUND, "entity":"", "error":"No hay datos en la base de datos"},\
             status= status.HTTP_404_NOT_FOUND)

class SubCategories(APIView):
    def get(self, req, id):
        try:
            subCategory = SubCategory.objects.values('id','name').get(id=id)
            aspects = Aspect.objects.values('id', 'objective').filter(sub_cat_id=id)
            return Response({"status": status.HTTP_200_OK, "entity": {'subcategory': subCategory, 'aspects': aspects} ,"error":""}, status = status.HTTP_200_OK)
        except KeyError:
            return Response({"status": status.HTTP_400_BAD_REQUEST, "entity": "", "error":"Campos ingresados de forma incorrecta"},\
             status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"status": status.HTTP_404_NOT_FOUND, "entity":"", "error":"No hay datos en la base de datos"},\
             status= status.HTTP_404_NOT_FOUND)

    def post(self, req):
        try:
            body = req.data
            id_teacher = body['id_teacher']
            id_category = body['id_category']
            option = body['option']

            if option == 0:
                #Crear una subcategoria
                print("Algo sucederá")
            elif option == 1:
                #Listar categorias
                subcats = SubCategory.objects.values('id', 'name').filter(category_id__teacher=id_teacher, category_id=id_category)
                return Response({"status": status.HTTP_200_OK, "entity": subcats, "error":""}, status = status.HTTP_200_OK)
        except KeyError:
             return Response({"status": status.HTTP_400_BAD_REQUEST, "entity": "", "error":"Campos ingresados de forma incorrecta"},\
             status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"status": status.HTTP_404_NOT_FOUND, "entity":"", "error":"No hay datos en la base de datos"},\
             status= status.HTTP_404_NOT_FOUND)

class Aspects(APIView):
    def get(self, req, id):
        try:
            aspect = Aspect.objects.values('id','objective').get(id=id)
            problems = Problem.objects.values('id', 'question').filter(aspect_id=id)
            return Response({"status": status.HTTP_200_OK, "entity": {'aspect': aspect, 'problems': problems} ,"error":""}, status = status.HTTP_200_OK)
        except KeyError:
            return Response({"status": status.HTTP_400_BAD_REQUEST, "entity": "", "error":"Campos ingresados de forma incorrecta"},\
             status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"status": status.HTTP_404_NOT_FOUND, "entity":"", "error":"No hay datos en la base de datos"},\
             status= status.HTTP_404_NOT_FOUND)

    def post(self, req):
        try:
            body = req.data
            id_teacher = body['id_teacher']
            id_category = body['id_category']
            id_subcat = body['id_subcat']
            option = body['option']

            if option == 0:
                #Crear un aspecto
                print("Algo sucederá")
            elif option == 1:
                #Listar categorias
                aspects = Aspect.objects.values('id', 'objective').filter(sub_cat_id = id_subcat, sub_cat_id__category_id__teacher=id_teacher, sub_cat_id__category_id=id_category)
                return Response({"status": status.HTTP_200_OK, "entity": aspects, "error":""}, status = status.HTTP_200_OK)
        except KeyError:
             return Response({"status": status.HTTP_400_BAD_REQUEST, "entity": "", "error":"Campos ingresados de forma incorrecta"},\
             status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"status": status.HTTP_404_NOT_FOUND, "entity":"", "error":"No hay datos en la base de datos"},\
             status= status.HTTP_404_NOT_FOUND)

class Problems(APIView):
    def get(self, req, id):
        try:
            problem = Problem.objects.values('id','question', 'answer').get(id=id)
            return Response({"status": status.HTTP_200_OK, "entity": {'problem': problem} ,"error":""}, status = status.HTTP_200_OK)
        except KeyError:
            return Response({"status": status.HTTP_400_BAD_REQUEST, "entity": "", "error":"Campos ingresados de forma incorrecta"},\
             status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"status": status.HTTP_404_NOT_FOUND, "entity":"", "error":"No hay datos en la base de datos"},\
             status= status.HTTP_404_NOT_FOUND)

    def post(self, req):
        try:
            body = req.data
            id_teacher = body['id_teacher']
            id_category = body['id_category']
            id_subcat = body['id_subcat']
            id_aspect = body['id_aspect']
            option = body['option']

            if option == 0:
                #Crear un aspecto
                print("Algo sucederá")
            elif option == 1:
                #Listar categorias
                problems = Problem.objects.values('id','question').filter(aspect_id__sub_cat_id = id_subcat, aspect_id__sub_cat_id__category_id__teacher=id_teacher, aspect_id__sub_cat_id__category_id=id_category, aspect_id=id_aspect)
                return Response({"status": status.HTTP_200_OK, "entity": problems, "error":""}, status = status.HTTP_200_OK)
        except KeyError:
             return Response({"status": status.HTTP_400_BAD_REQUEST, "entity": "", "error":"Campos ingresados de forma incorrecta"},\
             status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"status": status.HTTP_404_NOT_FOUND, "entity":"", "error":"No hay datos en la base de datos"},\
             status= status.HTTP_404_NOT_FOUND)

class Exams(APIView):

    def get(self, req, id):
        try:
            exam = Exam.objects.values('id', 'name', 'duration').get(id=id)
            tests = Test.objects.values('id','weight', 'aspect').filter(exam_id=id)
            questions = []
            problems_id = []

            for test in tests:
                problems = Problem.objects.values('id', 'question', 'answer').filter(aspect_id=test['aspect']).exclude(id__in=(problems_id))
                len_problems = len(problems)
                index = random.randint(0, len_problems-1)
                questions.append({
                    'question': problems[index],
                    'weight': test['weight']
                })
                problems_id.append(problems[index]['id'])
            return Response({"status": status.HTTP_200_OK, "entity": {'exam': exam, 'questions': questions} ,"error":""}, status = status.HTTP_200_OK)
        except KeyError:
            return Response({"status": status.HTTP_400_BAD_REQUEST, "entity": "", "error":"Campos ingresados de forma incorrecta"},\
             status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"status": status.HTTP_404_NOT_FOUND, "entity":"", "error":"No hay datos en la base de datos"},\
             status= status.HTTP_404_NOT_FOUND)

    """def get(self, req):
        try:
            exams = Exam.objects.values('id','name',"teacher__name")
            return Response({"status": status.HTTP_200_OK, "entity": exams ,"error":""}, status = status.HTTP_200_OK)
        except KeyError:
             return Response({"status": status.HTTP_400_BAD_REQUEST, "entity": "", "error":"Campos ingresados de forma incorrecta"},\
             status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"status": status.HTTP_404_NOT_FOUND, "entity":"", "error":"No hay datos en la base de datos"},\
             status= status.HTTP_404_NOT_FOUND)"""

    def post(self, req):
        try:
            body = req.data
            id_teacher = body['id_teacher']
            option = body['option']

            if option == 0:
                #Crear un examen
                print("Algo sucederá")
            elif option == 1:
                #Listar examenes de un profesor
                exams = Exam.objects.values('id','name').filter(teacher_id=id_teacher)
                return Response({"status": status.HTTP_200_OK, "entity": exams, "error":""}, status = status.HTTP_200_OK)
        except KeyError:
             return Response({"status": status.HTTP_400_BAD_REQUEST, "entity": "", "error":"Campos ingresados de forma incorrecta"},\
             status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"status": status.HTTP_404_NOT_FOUND, "entity":"", "error":"No hay datos en la base de datos"},\
             status= status.HTTP_404_NOT_FOUND)

class Tests(APIView):  
    def post(self, req):
        try:
            body = req.data
            id_exam = body['id_exam']
            option = body['option']

            if option == 0:
                #Crear un test
                print("Algo sucederá")
            elif option == 1:
                #Listar test de un examen
                test = Test.objects.values('id','exam__name',"aspect__objective","weight").filter(exam_id=id_exam)
                return Response({"status": status.HTTP_200_OK, "entity": test, "error":""}, status = status.HTTP_200_OK)
        except KeyError:
             return Response({"status": status.HTTP_400_BAD_REQUEST, "entity": "", "error":"Campos ingresados de forma incorrecta"},\
             status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"status": status.HTTP_404_NOT_FOUND, "entity":"", "error":"No hay datos en la base de datos"},\
             status= status.HTTP_404_NOT_FOUND)



