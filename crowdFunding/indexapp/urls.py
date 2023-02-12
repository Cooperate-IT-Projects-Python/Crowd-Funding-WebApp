from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('contact/', views.contact, name='contact'),
    path('report/', views.report, name='report'),
    path('single/', views.single, name='single'),

    path('donate/', views.donate, name='donate'),
]
