from django.urls import path
from . import views

urlpatterns = [
    path('', views.content),
    path('', views.team_matching),

]