from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('groups', views.Groups.as_view()),
    path('categories', views.Categories.as_view()),
    path('categories/<int:id>', views.Categories.as_view())
]