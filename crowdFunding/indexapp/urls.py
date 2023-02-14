from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='indexPage'),
    path('rate/<int:project_id>/<int:rating>/', views.rate, name='rating'),
    path('edit_user_profile/', views.edit_user_profile, name='edit_user_profile'),
    path('delete_user_profile/', views.delete_user_profile, name='delete_user_profile'),
    path('user_profile/', views.user_profile, name='user_profile'),
]
