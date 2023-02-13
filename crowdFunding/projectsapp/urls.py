from django.urls import path
from . import views
urlpatterns = [
   path('form/', views.projectForm, name='displayForm'),
   # path('create/', views.createProject, name='createProject'),
]
