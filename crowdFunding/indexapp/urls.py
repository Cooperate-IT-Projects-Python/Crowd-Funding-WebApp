from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='indexPage'),
    path('rate/<int:project_id>/<int:rating>/', views.rate, name='rating'),
]
