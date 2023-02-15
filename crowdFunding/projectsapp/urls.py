from django.urls import path
from . import views
urlpatterns = [
   path('form/', views.projectForm, name='displayForm'),
   path('makedonation/<int:project_id>', views.make_donation, name='makeDonation'),
   path('projectpage/<int:project_id>', views.project_page, name='projectPage'),
]
