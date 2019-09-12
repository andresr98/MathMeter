from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('groups', views.Groups.as_view()),
    path('categories', views.Categories.as_view()),
    path('categories/<int:id>', views.Categories.as_view()),
    path('subCategories', views.SubCategories.as_view()),
    path('subCategories/<int:id>', views.SubCategories.as_view()),
    path('aspects', views.Aspects.as_view()),
    path('aspects/<int:id>', views.Aspects.as_view()),
    path('problems', views.Problems.as_view()),
    path('problems/<int:id>', views.Problems.as_view()),
    path('exams', views.Exams.as_view()),
    path('exams/<int:id>', views.Exams.as_view()),
    path('tests', views.Tests.as_view()),
    path('studentAnswers', views.StudentAnswers.as_view()),
    path('studentsxgroups', views.StudensXGroups.as_view()),
]