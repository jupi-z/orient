from django.urls import path
from . import views
from .views import creer_questionnaire
from .views import prediction_view

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cursus/', views.cursus, name='cursus'),
    path('filiere/', views.filiere, name='filiere'),
    path('test/', views.test, name='test'),
    path('questionnaire/', creer_questionnaire, name='creer_questionnaire'),
    path('prediction/', prediction_view, name='prediction')
]
