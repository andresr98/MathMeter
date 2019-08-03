from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum

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
            #id_category = req.GET.get('id',0)
            category = Category.objects.values('id', 'name', 'description').filter(id=id)
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
                categories = Category.objects.values('name').filter(teacher_id=id_teacher)
                return Response({"status": status.HTTP_200_OK, "entity": categories, "error":""}, status = status.HTTP_200_OK)
        except KeyError:
             return Response({"status": status.HTTP_400_BAD_REQUEST, "entity": "", "error":"Campos ingresados de forma incorrecta"},\
             status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"status": status.HTTP_404_NOT_FOUND, "entity":"", "error":"No hay datos en la base de datos"},\
             status= status.HTTP_404_NOT_FOUND)