from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name='register'),
    path('logout/', views.logout_view, name='logout_view'),
    path('activate/<uid64>/<token>', views.activate, name="activate")

]
