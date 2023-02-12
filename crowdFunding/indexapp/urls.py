from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('contact/', views.contact, name='contact'),
    path('report/', views.report, name='report'),
    path('single/', views.single, name='single'),
    path('profile/', views.profile, name='profile'),

    path('donate/', views.donate, name='donate'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),

]
